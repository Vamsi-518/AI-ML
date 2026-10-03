import pandas as pd
from sklearn.preprocessing import StandardScaler
data = {
    "Age": [20, 25, 30, 35],
    "Marks": [60, 70, 80, 90]
}
df = pd.DataFrame(data)
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df)
result = pd.DataFrame(
    standardized_data,
    columns=df.columns
)
print("Original Data:")
print(df)
print("\nStandardized Data:")
print(result)