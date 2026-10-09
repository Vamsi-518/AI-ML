import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 45, 50, 60, 70, 75, 85, 90]
}
df = pd.DataFrame(data)
print("========== DATASET ==========")
print(df)
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
print("\n========== MODEL TRAINED ==========")
print("Linear Regression model trained successfully!")
y_pred = model.predict(X_test)
print("\n========== PREDICTIONS ==========")
print("Actual Values:")
print(list(y_test))
print("\nPredicted Values:")
print(list(y_pred))
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\n========== MODEL EVALUATION ==========")
print("MSE:", mse)
print("MAE:", mae)
print("R2 Score:", r2)
new_hours = [[9]]
new_prediction = model.predict(new_hours)
print("\n========== NEW PREDICTION ==========")
print("Study Hours:", new_hours[0][0])
print("Predicted Marks:", new_prediction[0])
plt.scatter(X, y)
plt.plot(
    X,
    model.predict(X)
)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
print("\n========== PROGRAM COMPLETED ==========")