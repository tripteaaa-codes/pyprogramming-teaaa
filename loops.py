 #WHILE LOOP
i = 0
while ( i<=5 ):
    print(i)
    i += 1
print("end of while loop")

#example: prime number between 1 to 100 
i = 1
while (i<=100):
    print(i)
    i += 1
print("end of while loop")

#FOR LOOP 
list = [1, 2, 3, 4, 5, 6]
for el in list:
    print(el)
print("end of for loop")

#example: list veggies using for loop.
veggies = ["potato", "tomato", "onion", "carrot"]
for i in veggies:
    print(i)
print("end of for loop")

#FOR LOOP WITH ELSE 
#example: list veggies using for loop with else.
nums = [1, 2, 3, 4, 5, 6]
for i in nums:
    print(i)
else:
    print("end of for loop with else")

#example: list veggies using for loop with else.
veggies = ["potato", "tomato", "onion", "carrot"]
for i in veggies:
    print(i  == "potato")
    if i == "potato":
        print("found potato")
        break
else:
    print("end of for loop with else")

#LOOP WITH RANGE FUNCTION
#range (stop)
for i in range(5):
    print(i)

#range (start, stop)
for i in range(5, 10):
    print(i)

#range (start, stop, step)
for i in range(2,10,2):
    print(i)


#LOOP WITH PASS STATEMENT
for i in range(5):
    pass

if i > 5:
    pass
print("end of pass statement")
