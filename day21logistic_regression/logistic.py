from sklearn.linear_model import LogisticRegression
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]
model = LogisticRegression()
model.fit(X, y)
print("Logistic Regression Model Created!")
print("Model Coefficient:", model.coef_)
print("Model Intercept:", model.intercept_)
print("Classes:", model.classes_)