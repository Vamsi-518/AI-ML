import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95],
    "Assignments": [20, 30, 40, 50, 65, 75, 85, 95],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]
print("Features (X):")
print(X)
print("\nTarget (y):")
print(y)