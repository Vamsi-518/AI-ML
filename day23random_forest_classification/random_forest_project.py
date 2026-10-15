import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 6, 7],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 55, 85, 90],
    "Assignments": [20, 30, 40, 50, 65, 75, 85, 95, 35, 45, 80, 90],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
print("========== DATASET ==========")
print(df)
X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=4,
    random_state=42
)
model.fit(X_train, y_train)
print("\nModel training completed!")
y_pred = model.predict(X_test)
print("\n========== PREDICTIONS ==========")
print("Actual:", list(y_test))
print("Predicted:", list(y_pred))
accuracy = accuracy_score(y_test, y_pred)
print("\n========== ACCURACY ==========")
print(f"Accuracy: {accuracy:.2%}")
print("\n========== CONFUSION MATRIX ==========")
print(confusion_matrix(y_test, y_pred, labels=[0, 1]))
print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Fail", "Pass"],
    zero_division=0
))
new_student = pd.DataFrame({
    "Hours": [6],
    "Attendance": [85],
    "Assignments": [80]
})
prediction = model.predict(new_student)[0]
print("\n========== NEW PREDICTION ==========")
print("Student Details:")
print(new_student)
print("Predicted Result:", "Pass" if prediction == 1 else "Fail")
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)
print("\n========== FEATURE IMPORTANCE ==========")
print(importance)
importance.plot(kind="bar")
plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()
print("\n========== PROJECT COMPLETED ==========")