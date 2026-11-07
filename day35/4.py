from sklearn.datasets import fetch_california_housing
import pandas as pd
housing = fetch_california_housing(as_frame=True)
df = housing.frame
print("Full table shape (districts, columns):", df.shape)
features = ['MedInc', 'HouseAge', 'AveRooms']
X_raw = df[features].copy()
print("\nFirst five rows:")
print(X_raw.head())
print("\nDataset Information:")
print(X_raw.info())
print("\nDescriptive Statistics:")
print(X_raw.describe())
print("\nMissing Values:")
print(X_raw.isnull().sum())
print("\nSelected Features:")
print(X_raw.columns.tolist())
