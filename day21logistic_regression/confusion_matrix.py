from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
matrix = confusion_matrix(
    y_test,
    y_pred,
    labels=[0, 1]
)
print("Confusion Matrix:")
print(matrix)
print("\nLabels: 0 = Fail, 1 = Pass")
print("Rows = Actual; Columns = Predicted")