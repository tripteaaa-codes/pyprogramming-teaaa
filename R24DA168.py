
# # Import Library
# import random

# # Step 1: Create Student Records
# students = []
# allocated = {}
# hall = []
# \

# # Function to Add Student Details
# def add_students():
#     n = int(input("Enter number of students: "))
#     for i in range(n):
#         name = input("Enter student name: ")
#         if name not in students:
#             students.append(name)
#         else:
#             print("Duplicate student not allowed")

# # Function to Allocate Seats
# def allocate_seats(rows, cols):
#     total = rows * cols
    
#     if len(students) > total:
#         print("Not enough seats in hall")
#         return False

#     seats = list(range(1, total + 1))
#     random.shuffle(seats)

#     for student in students:
#         if student not in allocated:
#             allocated[student] = seats.pop()
#     return True

# # Function to Generate Seating Chart
# def generate_chart(rows, cols):
#     global hall
#     hall = [["Empty" for _ in range(cols)] for _ in range(rows)]

#     for student, seat in allocated.items():
#         r = (seat - 1) // cols
#         c = (seat - 1) % cols
#         hall[r][c] = student

# # Function to Display Report
# def display_report():
#     print("\nStudent Seat Allocation")
#     for student, seat in allocated.items():
#         print(student, "-> Seat", seat)

#     print("\nHall Seating Chart")
#     for row in hall:
#         print(row)

# # Function to Export File
# def export_report():
#     file = open("exam_seating_report.txt", "w")
#     file.write("Exam Hall Seating Report\n")
#     for student, seat in allocated.items():
#         file.write(f"{student} -> Seat {seat}\n")
#     file.close()
#     print("\nSeating Report Exported Successfully!")

# # Main Program
# rows = int(input("Enter hall rows: "))
# cols = int(input("Enter hall columns: "))

# add_students()

# if allocate_seats(rows, cols):
#     generate_chart(rows, cols)
#     display_report()
#     export_report()/

# Smart Classroom Allocation System
# Using Excel Sheet + Random Library



# ========= Exam Seating Arrangement System =========#



import pandas as pd
import random

# Read Excel File
data = pd.read_csv("students.csv")

# Get Student Names
students = list(data["Name"])

# Shuffle Students Randomly
random.shuffle(students)

# Input Number of Classes
num_classes = int(input("Enter number of classes: "))

classes = {}

# Input Classroom Details
for i in range(num_classes):

    class_name = input(f"\nEnter class name {i+1}: ")

    benches = int(input("Enter number of benches: "))

    per_bench = int(input("Enter students per bench: "))

    total_seats = benches * per_bench

    classes[class_name] = {
        "benches": benches,
        "per_bench": per_bench,
        "total_seats": total_seats,
        "students": []
    }

# Allocate Students
remaining_students = students.copy()

for class_name, details in classes.items():

    seats = details["total_seats"]

    allocated = remaining_students[:seats]

    details["students"] = allocated

    remaining_students = remaining_students[seats:]

# Display Report
print("\n===== CLASSROOM ALLOCATION REPORT =====")

for class_name, details in classes.items():

    print(f"\nClass: {class_name}")
    print("Benches:", details["benches"])
    print("Students Per Bench:", details["per_bench"])

    index = 0

    for bench in range(1, details["benches"] + 1):

        print(f"\nBench {bench}: ", end="")

        for seat in range(details["per_bench"]):

            if index < len(details["students"]):
                print(details["students"][index], end="  ")
                index += 1

# Extra Students Shifted
if len(remaining_students) > 0:

    print("\n\n===== STUDENTS SHIFTED TO NEXT CLASS =====")

    for student in remaining_students:
        print(student)

else:
    print("\n\nAll students allocated successfully.")