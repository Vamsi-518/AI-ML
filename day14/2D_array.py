import numpy as np
students = np.array([
    [85, 90, 80],
    [70, 75, 80],
    [95, 90, 92]
])
print("Student Marks:")
print(students)
print("Shape:", students.shape)
print("First student:", students[0])
print("First student's first mark:", students[0, 0])