import pandas as pd
data = {
    "Name": ["Krishna", "Rahul", "Arjun", "Vijay"],
    "Age": [22, None, 23, 21],
    "Marks": [85, 72, None, 65]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print("\nAfter Handling Missing Values:")
print(df)