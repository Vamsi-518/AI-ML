from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
X = [
    [1, 40], [2, 45], [3, 50], [4, 60],
    [5, 70], [6, 80], [7, 90], [8, 95],
    [2, 50], [6, 85], [3, 55], [7, 88]
]
y = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
score = accuracy_score(y_test, y_pred)
print("Actual Results:", list(y_test))
print("Predicted Results:", list(y_pred))
print(f"Accuracy: {score:.2%}")