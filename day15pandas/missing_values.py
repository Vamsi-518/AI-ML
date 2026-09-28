import pandas as pd
students = pd.DataFrame({
    "Name": ["Krishna", "naga", "Arjun", "Vijay"],
    "Marks": [85, 72, None, 65]
})
print("Original Data:")
print(students)
print("\nMissing Values:")
print(students.isnull().sum())
students["Marks"] = students["Marks"].fillna(0)
print("\nAfter Filling Missing Values:")
print(students)