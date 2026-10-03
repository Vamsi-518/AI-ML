import pandas as pd
data = {
    "Name": ["Krishna", "Rahul", "Arjun", "Vijay"],
    "Gender": ["Male", "Male", "Male", "Male"]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})
print("\nEncoded Data:")
print(df)