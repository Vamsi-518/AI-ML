import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = {
    "Marks": [20, 40, 60, 80, 100]
}
df = pd.DataFrame(data)
scaler = MinMaxScaler()
df["Normalized_Marks"] = scaler.fit_transform(
    df[["Marks"]]
)
print(df)