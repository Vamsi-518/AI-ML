import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3],
    "Marks": [20, 30, 40, 50, 60, 70, 80, 90, 35, 45],
    "Result": [0, 0, 0, 1, 1, 1, 1, 1, 0, 0]
}
df = pd.DataFrame(data)
print("Classification Dataset:")
print(df)
print("\nDataset Information:")
print(df.info())
print("\nDataset Statistics:")
print(df.describe())