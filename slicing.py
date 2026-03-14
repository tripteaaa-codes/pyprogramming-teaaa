#slicing
str = "tripti kashyap"
print(str[3:6]) 
print(str[0:len(str)]) 
print(str[0:len(str):2])

#negative slicing
print(str[-1])
print(str[-2:-5])
print(str[2:4:7])

#string functions
print(str.endswith("a"))
print(str.capitalize())
print(str.replace("ti","teaaa"))
print(str.find("p"))
print(str.count("a"))