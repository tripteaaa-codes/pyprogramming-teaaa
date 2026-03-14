#ELSE example
age = 21

if (age >= 18):
    print("eligible to vote")
else:
    print("Not eligible to vote")


#ELIF example
if (age < 18):
    print("Not eligible to vote")
elif (age == 18):
    print("eligible to vote")
elif (age > 18 and age < 60):
    print("eligible to vote")

#IF example
if (age < 18):
    print("Not eligible to vote")
if (age == 18):
    print("eligible to vote")
if (age > 18):
    print("eligible to vote")

#NESTED IF example
age = 21
if (age >= 18):
    if (age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else: 
    print("cannot drive")