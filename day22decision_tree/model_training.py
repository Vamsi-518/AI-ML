import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 7],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 90],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Attendance"]]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
model.fit(X_train, y_train)
print("Model Training Completed!")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))