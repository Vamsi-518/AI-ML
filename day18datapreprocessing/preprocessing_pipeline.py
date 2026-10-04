import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

data = {
    "Age": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "Marks": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 200],
    "Height": [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161],
    "Result": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Select input features separately from the target.
X = df[["Age", "Marks", "Height"]]
y = df["Result"]

# Split before fitting preprocessing steps to avoid data leakage.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Use training-set IQR bounds to cap outliers in both datasets.
Q1 = X_train.quantile(0.25)
Q3 = X_train.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
X_train = X_train.clip(lower=lower, upper=upper, axis=1)
X_test = X_test.clip(lower=lower, upper=upper, axis=1)

# Fit normalization on training features, then reuse it for test features.
scaler = MinMaxScaler()
X_train = pd.DataFrame(
    scaler.fit_transform(X_train),
    columns=X.columns,
    index=X_train.index
)
X_test = pd.DataFrame(
    scaler.transform(X_test),
    columns=X.columns,
    index=X_test.index
)

print("Training Features:")
print(X_train)
print("\nTesting Features:")
print(X_test)
print("\nTraining Labels:")
print(y_train)
print("\nTesting Labels:")
print(y_test)
