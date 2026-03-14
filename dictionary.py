dict = {
    "student" : "tripti",
     "cgpa" : 8.5,
     "marks" : 90,
     "grade" : "A",
     "college" : "reva university",
}

print(dict)


#accessing single value

# print(dict["student"])
# print(dict["cgpa"])
# print(dict["marks"])

# #nested dictionary
# dict1 = {
#     "student" : {
#         "name" : "tripti",
#         "cgpa" : 8.5,
#         "marks" : 90,
#     },
#     "teacher" : {
#         "name" : "suman",
#         "cgpa" : 9.5,
#         "marks" : 95,
#     }
# }

# print(dict1)
# print(dict1["student"])
# print(dict1["teacher"])

#dictionary methods

#copy
print(dict.keys())
#values
print(dict.values())
#items
print(dict.items())
#get
print(dict.get("student"))
#update
dict.update({"cgpa" : 9.0})
print(dict)