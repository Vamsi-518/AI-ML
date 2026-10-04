import pandas as pd
data = {
    "Age": [20, 21, 22, 23],
    "Marks": [60, 70, 80, 90],
    "Height": [165, 170, 175, 180],
    "Result": [0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Age", "Marks", "Height"]]
y = df["Result"]
print("Selected Features:")
print(X)
print("\nTarget:")
print(y)