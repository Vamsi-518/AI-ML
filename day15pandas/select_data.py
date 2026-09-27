import pandas as pd
students = pd.DataFrame({
    "Name": ["Krishna", "naga", "murali", "Vamsi"],
    "Age": [22, 21, 23, 22],
    "Marks": [85, 72, 91, 65]
})
print("Names:")
print(students["Name"])
print("\nFirst Student:")
print(students.iloc[0])
print("\nFirst Two Students:")
print(students.iloc[:2])
print("\nFirst Three Students:")
print(students.iloc[:3])
print("\nFirst Four Students:")
print(students.iloc[:4])