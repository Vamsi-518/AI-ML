import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Sleep": [8, 7, 7, 6, 6, 5],
    "Marks": [35, 45, 50, 60, 70, 80]
}
df = pd.DataFrame(data)
X = df[["Hours", "Sleep"]]
y = df["Marks"]
model = LinearRegression()
model.fit(X, y)
print("Multiple Linear Regression")
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
prediction = model.predict([[7, 6]])
print("\nPredicted Marks:")
print(prediction[0])