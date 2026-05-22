import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "student" : [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    "marks" : [80, 45, 68, 90, 66, 44, 85, 72],
    "attendance" : [85, 77, 90, 86, 55, 78, 72, 70]
})

fig = px.scatter_3d(df,
                    x = "student",
                    y = "marks",
                    z = "attendance",  
                    title = "3D Student Analysis")
fig.show()

# plt.bar(student, marks)
# plt.title(" GRAPH OF STUDENT MARKS")
# plt.xlabel("student")
# plt.ylabel("marks")
# plt.grid()
# plt.show()