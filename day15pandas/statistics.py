import pandas as pd
students = pd.DataFrame({
    "Name": ["Krishna", "Rahul", "Arjun", "Vijay"],
    "Marks": [85, 72, 91, 65]
})
print("Total:", students["Marks"].sum())
print("Average:", students["Marks"].mean())
print("Maximum:", students["Marks"].max())
print("Minimum:", students["Marks"].min())