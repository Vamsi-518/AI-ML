import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = {
    "Age": [20, 25, 30, 35],
    "Salary": [20000, 40000, 60000, 80000]
}
df = pd.DataFrame(data)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)
print("Original Data:")
print(df)
print("\nScaled Data:")
print(scaled_df)