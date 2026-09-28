import pandas as pd
students = pd.DataFrame({
    "Name": ["Krishna", "Rahul", "Arjun", "Vijay"],
    "Marks": [85, 72, 91, 65]
})
top_students = students[
    students["Marks"] >= 80
]
print("Students with marks >= 80:")
print(top_students)