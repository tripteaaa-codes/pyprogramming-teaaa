# Import Library
import random

# Step 1: Create Student Records
students = []
allocated = {}
hall = []

# Function to Add Student Details
def add_students():
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter student name: ")
        if name not in students:
            students.append(name)
        else:
            print("Duplicate student not allowed")

# Function to Allocate Seats
def allocate_seats(rows, cols):
    total = rows * cols
    
    if len(students) > total:
        print("Not enough seats in hall")
        return False

    seats = list(range(1, total + 1))
    random.shuffle(seats)

    for student in students:
        if student not in allocated:
            allocated[student] = seats.pop()
    return True

# Function to Generate Seating Chart
def generate_chart(rows, cols):
    global hall
    hall = [["Empty" for _ in range(cols)] for _ in range(rows)]

    for student, seat in allocated.items():
        r = (seat - 1) // cols
        c = (seat - 1) % cols
        hall[r][c] = student

# Function to Display Report
def display_report():
    print("\nStudent Seat Allocation")
    for student, seat in allocated.items():
        print(student, "-> Seat", seat)

    print("\nHall Seating Chart")
    for row in hall:
        print(row)

# Function to Export File
def export_report():
    file = open("exam_seating_report.txt", "w")
    file.write("Exam Hall Seating Report\n")
    for student, seat in allocated.items():
        file.write(f"{student} -> Seat {seat}\n")
    file.close()
    print("\nSeating Report Exported Successfully!")

# Main Program
rows = int(input("Enter hall rows: "))
cols = int(input("Enter hall columns: "))

add_students()

if allocate_seats(rows, cols):
    generate_chart(rows, cols)
    display_report()
    export_report()
