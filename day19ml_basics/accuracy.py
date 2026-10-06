from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X = [[1], [2], [3], [4], [5], [6]]
y = [35, 45, 50, 60, 70, 80]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)
print("Actual Values:")
print(y_test)
print("\nPredicted Values:")
print(y_pred)
print("\nR2 Score:")
print(score)