import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [20, 30, 40, 50, 60, 70],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Marks"]]
y = df["Result"]
print("Features (X):")
print(X)
print("\nTarget (y):")
print(y)