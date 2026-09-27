import pandas as pd
students = pd.DataFrame({
    "Name": ["Krishna", "Rama", "Arun", "Vijay"],
    "Marks": [85, 72, 91, 65]
})
students["Result"] = [
    "Pass",
    "Pass",
    "Pass",
    "Pass"
]
print(students)