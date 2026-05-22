import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px 


# x = [1, 2, 3]
# y = [4, 5, 6]

# # plt.plot(x, y)
# # plt.grid()
# # plt.show()

# #univariate - Numerical
# data = {
#     "Salary" : [ 25000, 30000, 37000, 28000, 48000, 55000, 52000, 35000, 26000, 27000, 31000, 32000, 23000, 34000, 44000, 59000]
# }
# df = pd.DataFrame(data)

# # print(df.head())
# # print(df.shape)

# # plt.plot(df["Salary"])
# # plt.show()

# # #line-plot
# # plt.plot(df["Salary"], color = "red", marker = "o", linestyle = ":", linewidth = "2")
# # plt.grid()
# # plt.show()

# # #histogram
# # plt.hist(df["Salary"], bins = 5, color = "pink")
# # plt.show()

# # #boxplot
# # plt.boxplot(df["Salary"])
# # plt.show()
# # # df.loc[20] = [0]
# # # df.drop(index = 20, inplace = True)
# # print(df.shape)

# #univariate: categorical
# dept_list = ['HR', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'] * 2
# df["dept"] = (dept_list * len(df))[:len(df)]
# print(df.shape)
# (df.head())

# #pie chart:
# # count = df["dept"].value_counts()
# # plt.pie(count, labels = count.index, autopct = "%1.0f", explode=[0.1,0.1,0.1])
# # plt.title("Department Department")
# # plt.axis("equal")
# # plt.show()

# #countplot
# # plt.bar(count.index, count, color = ["green", "black", "red"])
# # plt.show()


# df["Age"] = [22,25,29,30,35,40,36,28,22,23,25,29,33,36,40,22]

# sort_age = df.sort_values("Age")

# #scatter-plot
# # plt.scatter(sort_age["Age"], sort_age["Salary"], color = "orange")
# # plt.xlabel("Age")
# # plt.ylabel("Salary")
# # plt.show()

# # #line-plot
# # plt.plot(sort_age["Age"], sort_age["Salary"], color = "red", marker = "*", linestyle = ":", linewidth = 2)
# # plt.grid()
# # plt.show()

# #bar-chart
# # plt.bar(sort_age["Age"], df["Salary"], color = "green", align = "center") 
# # plt.show()

# #bivariate: numerical-categorical
# # hr_sal = df[df["dept"] == "HR"]["Salary"]
# # hr_sal

# # it_sal = df[df["dept"] == "IT"]["Salary"]
# # it_sal

# # fin_sal = df[df["dept"] == "Finance"]["Salary"]

# # #boxplot
# # plt.boxplot([hr_sal, it_sal, fin_sal], labels = ["HR", "IT", "Fianace"])
# # plt.show()

# # #pie-chart
# # salary_by_dept = df.groupby("dept")["Salary"].mean()
# # salary_by_dept

# # plt.pie(salary_by_dept, labels = salary_by_dept.index, autopct = "%1.2f")
# # plt.axis("equal")
# # plt.show()

# #bar-plot
# # hr_mean = sum(hr_sal)/len(hr_sal)
# # it_mean = sum(it_sal)/len(it_sal)
# # fin_sal = sum(fin_sal)/len(fin_sal)

# # plt.bar(["HR", "IT", "Finance"], [hr_mean, it_mean, fin_sal], color = ["green", "black", "red"])
# # plt.show()

# #multivariate analysis: 3 numerical columns
# df["experience"] = [1,2,4,1.5,5,5,8,12,10,1,1.2,2,3,1.8,5.5,4.5]
# df.head()

# # bubble-plot
# # plt.scatter(df["Age"], df["Salary"], s = df["experience"]*15, color = "pink", edgecolors = "black")
# # plt.title("Age vs Salary vs Experience")
# # plt.xlabel("Age")
# # plt.ylabel("Salary")
# # plt.grid()
# # plt.show()

# # # 2 numerical and 1 categorical column:
# # plt.scatter(df["Age"], df["Salary"], c = df["dept"].map({"HR" : "yellow", "IT" : "red", "Finance" : "pink"}), label = ["HR", "IT", "Finance"])
# # plt.xlabel("Age")
# # plt.ylabel("Salary")
# # plt.title("Age vs Salary vs Dept")
# # plt.legend()
# # plt.show()

# # color = {"HR" : "yellow", "IT" : "red", "Finance" : "pink"}

# # for dept, color in color.items():
# #     df_dept = df[df["dept"] == dept]
# #     plt.scatter(df_dept["Age"], df_dept["Salary"], c = color, label = dept)
# #     plt.grid()
# #     plt.legend()
# #     plt.show()

# #object-oriented API
# fig, axs = plt.subplots(1,3, figsize = (10,5))


# #line-plot
# # axs[0].plot(sort_age["Age"], df["Salary"], color = 'red', marker = "*", linewidth = "2", markersize = 2)
# # axs[0].grid()
# # axs[0].set_title("Line plot")
# # axs[0].set_xlabel("Age")
# # axs[0].set_ylabel("Salary")

# # #histogram
# # axs[1].hist(df["Salary"], bins = 5, color = "pink")
# # axs[1].set_title("Histogram")
# # axs[1].set_xlabel("Salary")
# # axs[1].set_ylabel("Frequency")

# # #boxplot
# # axs[2].boxplot(df["Salary"])
# # axs[2].set_title("Boxplot")
# # axs[2].set_xlabel("Salary")
# # plt.tight_layout()
# # plt.show()

# #financial-data
# data = {
#     'Year': [2020, 2021, 2022, 2023],
#     'Sales': [100, 150, 250, 300],
#     'Profit': [20, 30, 40 ,50],
#     'Expenses': [80, 120, 160, 200]
# }

# df2 = pd.DataFrame(data)
# plt.plot(df2["Year"], df2["Sales"], label = "Sales")
# plt.plot(df2["Year"], df2["Profit"], label = "Profit")
# plt.plot(df2["Year"], df2["Expenses"], label = "Expenses")

# plt.title("Financial Analysis")
# plt.xlabel("Year")
# plt.ylabel("Amount")
# plt.legend()
# plt.show()

# #3D
# fig = px.scatter_3d(df, x = "Age", y = "Salary", z = "experience", title = "3D Scatter Plot")
# fig.show()
                            #    or    #    
# # ax = plt.axes(projection = "3d")
# # ax.scatter(df["Age"], df["Salary"], df["experience"])
# # ax.set_xlabel("Age")
# # ax.set_ylabel("Salary")
# # ax.set_zlabel("Experience")
# # plt.show()