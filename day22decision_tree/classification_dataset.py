import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 6],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 85],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
print("AI/ML Classification Dataset:")
print(df)
print("\nDataset Shape:")
print(df.shape)
print("\nDataset Statistics:")
print(df.describe())