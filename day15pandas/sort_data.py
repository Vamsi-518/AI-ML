import pandas as pd
students = pd.DataFrame({
    "Name": ["Krishna", "Rahul", "Arjun", "Vijay"],
    "Marks": [85, 72, 91, 65]
})
sorted_students = students.sort_values(
    by="Marks",
    ascending=False
)
print("Students sorted by marks:")
print(sorted_students)