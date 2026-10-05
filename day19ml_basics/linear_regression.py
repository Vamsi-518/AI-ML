from sklearn.linear_model import LinearRegression
X = [[1], [2], [3], [4], [5], [6]]
y = [35, 45, 50, 60, 70, 80]
model = LinearRegression()
model.fit(X, y)
print("Model created successfully!")
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)