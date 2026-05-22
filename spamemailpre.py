import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    "email" : [
        "Win money now",
        "Limited offer just for you",
        "Meeting at 3pm",
        "Myntra fashion offer",
        "College unifest datelist",
        "Project discussion at 10am"
    ],
    "label" : [1,1,0,0,1,0]
}

df = pd.DataFrame(data)

X = df["email"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

X_train_vec = vectorizer.transform(X_test)
predictions = model.predict(X_train_vec)

print("Predications:", predictions)