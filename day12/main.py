# main.py
from student import student_details, add_marks
from student_package.details import college_details, course_details
print("==== MODULE ====")
student_details(
    "Krishna",
    22,
    "Python Full Stack"
)
total = add_marks(85, 90)
print("Total Marks:", total)
print("\n==== PACKAGE ====")
college_details()
course_details()
print("\n==== PROGRAM COMPLETED ====")