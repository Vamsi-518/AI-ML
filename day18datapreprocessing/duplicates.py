import pandas as pd
data = {
    "Name": ["Krishna", "Rahul", "Arjun", "Krishna"],
    "Marks": [85, 72, 91, 85]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
df = df.drop_duplicates()
print("\nAfter Removing Duplicates:")
print(df)