#Separate the dataset into features (X) and target (y).

import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 45, 50, 60, 70, 80]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
print("Features (X):")
print(X)
print("\nTarget (y):")
print(y)