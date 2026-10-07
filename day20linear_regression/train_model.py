import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 45, 50, 60, 70, 75, 85, 90]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
print("Model Training Completed!")
print("\nTraining Data:")
print(X_train)
print("\nTesting Data:")
print(X_test)