import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 45, 50, 60, 70, 80]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
model = LinearRegression()
model.fit(X, y)
print("Simple Linear Regression")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
prediction = model.predict([[7]])
print("\nPredicted marks for 7 hours:")
print(prediction[0])