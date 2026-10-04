import pandas as pd
data = {
    "Marks": [50, 55, 60, 65, 70, 75, 200]
}
df = pd.DataFrame(data)
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[
    (df["Marks"] < lower) |
    (df["Marks"] > upper)
]
print("Outliers:")
print(outliers)