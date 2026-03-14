print ("Enter the number")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("choose operation (+, -, *, /): ")

if operation == "+":
    print("result", num1 + num2)

elif operation == "-":
    print("Result", num1 - num2)

elif operation == "*":
    print("Result", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result", num1 / num2)
    else:
        print("cannot divided by zero")
else:
    print("Invalid operation")
