# QUESTION1
# WAP to input users first name and print its length.
# name = input("Enter your first name: Tripteaaa")
# print("Length of your first name is:", len(name))


# QUESTION2
# #WAP to find the occurance of $ in a string.
# str = "tripti kashyap$"
# print(str.count("$"))


#QUESTION3
# WAP to grade students based on marks.
# marks = int(input("Enter your marks: "))
# if (marks >= 90): 
#      grade = "A"
# elif (marks >= 80):
#      grade = "B"
# elif (marks >= 70):
#      grade = "C"
# elif (marks >= 60):
#      grade = "D"
# else:
#      grade = "E"
#  print("Your grade is:", grade)
    

#QUESTION4
# WAP to check if a number entered by user is odd or even.
# num = int(input("Enter a number: "))
# if(num % 2 == 0):
#     print("Even number")
# else:
#     print("Odd number")


#QUESTION5
# WAP tp ask the user to enter name of their 3 favorite movies & store them in a list.
# movies = []
# movies.append(input("Enter your favorite movie 1: "))
# movies.append(input("Enter your favorite movie 2: "))
# movies.append(input("Enter your favorite movie 3: "))
# print("movies")


#QUESTION6
# WAP tp check if a list contains a palindrome of elements.
# list1 = ["m" , "a", "d", "a", "m"]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if (copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#QUESTION7
# WAP to count the number of students with the "A" grade.
# grade = ["A", "B", "C", "A", "D", "A", "A" , "A", "B", "C", "A", "D", "A", "A" , "A"]
# print(grade.count("A"))
# grade.sort()
# print(grade)


#QUESTION7 (LOOPS EXAMPLE)
#WAP to print  numbers from 1 to 100.
# 
# i = 1
# while (i <= 100):
#     print (i)
#     i += 1
# print("end of while loop")


#QUESTION8 (LOOPS EXAMPLE)
#WAP to print number from 100 to 1.
# i = 100
# while (i >=1):
#     print(i)
#     i -= 1
# print("end of while loop")


#QUESTION9 (LOOPS EXAMPLE)
#WAP to print multiplication table of a number of a number n.
# n = int(input("Enter a number: "))
# i = 1
# while (i <= 10):
#     print(n*i)
#     i += 1


#QUESTION10 (LOOPS EXAMPLE)
#WAP to print the elements of a list using for loop.
#nums = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]
# i = 0
# while (i < len(nums)):
#       print(nums[i])
#       i += 1


#QUESTION11 (LOOPS EXAMPLE)
#WAP to search for a number x in this tuple using loop.
# nums = (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)
# x = 25
# i = 0
# while (i < len(nums)):
#     if (nums[i] == x):
#         print("Found")
#         break
#     i += 1
#     else:
#         print("Not Found")


#QUESTION12 (LOOPS RANGE EXAMPLE)
# #WAP to print the number from 1 to 100 using range function.
# for i in range(1, 101):
#     print(i)

#QUESTION13
#WAP to print the number from 100 to 1 using range function.
# for i in range(100, 0, -1):
#     print(i)

#QUESTION14
#WAP to print the multiplication table of a number n using range function.
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n*i)

#QUESTION15
#WAP to find the sum of first n numbers using while.
# n = 7
# sum = 0
# i = 1
# while (i <= n):
#     sum += i
#     i += 1
# print("Sum of first", n, "numbers is:", sum)

#QUESTION16 
#WAP to find the factorial of first n numbers using for loop.
# n = 9
# factorial = 1
# i = 1
# for i in range(1, n+1):
#     factorial *= i
# print("Factorial of", n, "is:", factorial)


#QUESTION17 (FUNCTION EXAMPLE)
#WAF to print the length of a list.
# cities = ["bihar", "delhi", "mumbai", "kolkata", "chennai"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print()

#WAF to print the elements of a list in a single line.
# cities = ["bihar", "delhi", "mumbai", "kolkata", "chennai"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for items in list:
#         print(items, end=" ")

# print_list(cities)
# print() 

#WAF to find the factorial of a 7 using range.
factorial = 1
for i in range (1 , 8):
    factorial *= i
    print("Factorial of 7:", factorial)

#WAF to find factorial pf n using loop.
n = int(input("Enter a number: "))
factorial = 1
for i in range (1, n+1):
    factorial *= i
    print("Factorial of", n, "is" , factorial)
