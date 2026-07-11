# #Python function that accepts two integer numbers. 
# # If the product of the two numbers is less than or equal to 1000, 
# # return their product; otherwise, return their sum n1 = int(20)

# # n2 = int(30)
# # product = n1 * n2
# # if product <= 1000:
# #     print(product)
# # else:
# #     print(n1 + n2)

# # Iterate through the first 10 numbers (0–9). 
# # In each iteration, print the current number, the previous number, and their sum.

# # pre_num = int(0)
# # for i in range(10):
# #     sum = pre_num + i
# #     print(f"curr: {i}, pre sum: {pre_num}, sum: {sum}")
# #     pre_num = i

# # Display only those characters which are present at an even index number in given string.

# # s = "pynativr"
# # print("Original String:", s)
# # for i in range(0, len(s), 2):
# #     print(s[i])

# # Write a function to remove characters from a string starting from index 0 up to n and return a new string.

# # s  = "pynative"
# # remove_chars = s[4:8]
# # remove_chars1 = s[2:8]

# # print("Original String:", s)
# # print("String after removing characters:", remove_chars)
# # print("String after removing characters:", remove_chars1)
# # or
# # def remove_chars(word, n):
# #     print("Original String:", word)
# #     res = word[n:]
# #     print("String after removing characters:", res)
# #     print("String after removing characters:", word[4:])
# #     print("String after removing characters:", word[2:])

# # Write a program to swap the values of two variables, a and b, without using a third temporary variable.

# # a = 5
# # b = 10
# # print("Before swapping: a =", a, "b =", b)

# # a, b = b, a
# # print("After swapping: a =", a, "b =", b)

# # Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
# # n = 5
# # fact = 1
# # for i in range(1, n+1):
# #     fact *= i
# # print(f"Factorial of {n} is {fact}")

# # Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
# # fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# # fruits.append("fig")
# # print("After adding a new fruit:", fruits)
# # fruits.pop(1)
# # print("After removing the second fruit:", fruits)

# # Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
# # text = "Python"
# # print("Original String:", text)
# # reversed_s = text[::-1]
# # print("Reversed String:", reversed_s)

# # Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
# # sen = "Learning Python is fun!"
# # vowels = "aeiou"
# # count = 0
# # for char in sen.lower():
# #     if char in vowels:
# #         count += 1
# # print(f"Total number of vowels in the sentence:", count)

# # Given a list of integers, find and print both the largest and the smallest numbers.
# # nums = [45, 2, 89, 12, 7]
# # print("Largest number:", max(nums))
# # print("Smallest number:", min(nums))

# # Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
# # data = [1, 2, 2, 3, 4, 4, 4, 5]
# # unique_data = list(set(data))
# # print("Original List:", data)
# # print("List with unique elements:", unique_data)

# # Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
# # def check_first_last(lst):
# #     print("Original List:", lst)

# #     first_num = lst[0]
# #     last_num = lst[-1]

# #     if first_num == last_num:
# #         return True
# #     else:
# #         return False
# # numbers_x = [10,20, 30, 40, 50]
# # print("result is", check_first_last(numbers_x))
# # numbers_y = [75, 20, 30, 40, 10]
# # print("result is", check_first_last(numbers_y))

# # Iterate through a given list of numbers and print only those numbers which are divisible by 5.
# # num_list = [10, 20, 33, 46, 55]
# # print("given list", num_list)
# # print("Divisible by 5:")
# # for num in num_list:
# #     if num % 5 == 0:
# #         print(num)

# # Write a program to find how many times the substring “Emma” appears in a given string.
# # str_x = "Emma is good developer. Emma is a writer"
# # count = str_x.count("Emma")
# # print(f"Emma appeared {count} times")

# # Print the following pattern where each row contains a number repeated a specific number of times based on its value.
# # for num in range(1, 6):
# #     for i in range(num):
# #         print(num, end=" ")
# #     print("\n")

# # Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
# # def check_pal(num):
# #     print("Original num", num)

# #     original_str = str(num)
# #     rev_str = original_str[::-1]

# #     if original_str == rev_str:
# #         print("palindrome")
# #     else:
# #         print("not palindrome")
# # check_pal(121)
# # check_pal(125)

# # Create a new list from two given lists such that the new list contains 
# # odd numbers from the first list and even numbers from the second list.
# # def merge_list(list1, list2):
# #     result_list = []

# #     for num in list1:
# #         if num % 2 != 0:
# #             result_list.append(num)
# #     for num in list2:
# #         if num % 2 == 0:
# #             result_list.append(num)
    
# #     return result_list

# # list1 = [10, 20, 25, 30, 35]
# # list2 = [40, 45, 60, 75, 90]
# # print("result list:", merge_list(list1, list2))

# #  Write a program to extract each digit from an integer in the reverse order.
# # n = 7536
# # total = 0
# # rev = 0
# # print("given number:", n)
# # while n > 0:
# #     dig = n % 10
# #     rev = rev*10 + dig
# #     n//= 10
# # print("reverse of the given number is:", rev)

# # n = 7536
# # print("given number is:", n)
# # while n > 0:
# #     digit = n % 10
# #     n = n // 10
# #     print(digit, end="")

# # Calculate income tax for a given income based on these rules:
# # First $10,000: 0% tax
# # Next $10,000: 10% tax
# # Remaining income: 20% tax

# # income = 45000
# # tax = 0
# # print("Given income", income)
# # if income <= 10000:
# #     tax = 0
# # elif income <= 20000:
# #     tax = (income - 10000) * 10 / 100
# # else:
# #     tax = 0 + (10000 * 10/100)
# #     tax += (income - 20000) * 20/100
# # print("Total income tax to pay is", tax)

# Print a multiplication table from 1 to 10 in a formatted grid.

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end="\t")
#     print("\n")

# Print a downward half-pyramid pattern using stars (*).

# for i in range(5,0,-1):
#     for j in range(0, i):
#         print("*", end=" ")
#     print("\n")


# nums = [12,45,67,23,89,34]

# first = second =  third = float('-inf')

# for num in nums:
#     if num > first:
#         third = second
#         second = first
#         first = num 
#     elif first > num > second:
#         third = second
#         second = num
#     elif first > num > third:
#         third = num
# print(third)