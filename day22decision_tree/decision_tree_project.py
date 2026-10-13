import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 7, 3, 6],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 90, 55, 85],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
print("========== DATASET ==========")
print(df)
X = df[["Hours", "Attendance"]]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)
model.fit(X_train, y_train)
print("\nModel training completed!")
y_pred = model.predict(X_test)
print("\n========== PREDICTIONS ==========")
print("Actual:", list(y_test))
print("Predicted:", list(y_pred))
print("\n========== MODEL EVALUATION ==========")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=[0, 1]))
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Fail", "Pass"],
    zero_division=0
))
new_student = pd.DataFrame({
    "Hours": [6],
    "Attendance": [85]
})
prediction = model.predict(new_student)[0]
print("\n========== NEW PREDICTION ==========")
print("Study Hours:", new_student["Hours"].iloc[0])
print("Attendance:", new_student["Attendance"].iloc[0])
print("Predicted Result:", "Pass" if prediction == 1 else "Fail")
plt.figure(figsize=(12, 7))
plot_tree(
    model,
    feature_names=["Hours", "Attendance"],
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True
)
plt.title("Day 22 - Decision Tree Classifier")
plt.tight_layout()
plt.show()
print("\n========== PROJECT COMPLETED ==========")