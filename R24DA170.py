# Student Course Registration System

import pandas as pd

# -------------------------------
# Course Data
# -------------------------------
courses = {
    "CS101": {"name": "Python Programming", "credits": 4},
    "CS102": {"name": "Data Structures", "credits": 3},
    "CS103": {"name": "Database Systems", "credits": 3},
    "CS104": {"name": "Computer Networks", "credits": 2}
}

# -------------------------------
# Student Class
# -------------------------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.registered_courses = []

    # Register Course
    def register_course(self, course_code):
        if course_code in self.registered_courses:
            print(f"Course {course_code} already registered.")
        elif course_code in courses:
            self.registered_courses.append(course_code)
            print(f"Course {course_code} registered successfully.")
        else:
            print("Invalid Course Code")

    # Calculate Total Credits
    def total_credits(self):
        total = 0
        for code in self.registered_courses:
            total += courses[code]["credits"]
        return total

    # Generate Report
    def generate_report(self):
        print("\n------ Registration Report ------")
        print("Student ID :", self.student_id)
        print("Student Name :", self.name)
        print("\nRegistered Courses:")

        for code in self.registered_courses:
            print(code, "-", courses[code]["name"],
                  "-", courses[code]["credits"], "Credits")

        print("\nTotal Credits :", self.total_credits())


# -------------------------------
# Display Available Courses
# -------------------------------
def display_courses():
    print("\nAvailable Courses")
    print("----------------------------")
    for code, details in courses.items():
        print(code, "-", details["name"],
              "-", details["credits"], "Credits")


# -------------------------------
# Main Program
# -------------------------------
student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")

student = Student(student_id, student_name)

display_courses()

# Register Courses
while True:
    course = input("\nEnter Course Code to Register (or type 'exit'): ")

    if course.lower() == "exit":
        break

    student.register_course(course)

# Generate Report
student.generate_report()

# -------------------------------
# Store Data using DataFrame
# -------------------------------
data = {
    "Student ID": [student.student_id],
    "Student Name": [student.name],
    "Courses": [", ".join(student.registered_courses)],
    "Total Credits": [student.total_credits()]
}

df = pd.DataFrame(data)

print("\nStudent Record DataFrame")
print(df)

# Save to CSV File
df.to_csv("student_registration.csv", index=False)

print("\nData saved to student_registration.csv")
