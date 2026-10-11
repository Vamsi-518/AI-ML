import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 7],
    "Marks": [20, 30, 40, 50, 60, 70, 80, 90, 35, 85],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
print("========== DATASET ==========")
print(df)
X = df[["Hours", "Marks"]]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
model = LogisticRegression()
model.fit(X_train, y_train)
print("\nModel training completed!")
y_pred = model.predict(X_test)
print("\n========== PREDICTIONS ==========")
print("Actual:", list(y_test))
print("Predicted:", list(y_pred))
accuracy = accuracy_score(y_test, y_pred)
print("\n========== ACCURACY ==========")
print(f"{accuracy * 100:.2f}%")
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
    "Marks": [75]
})
prediction = model.predict(new_student)[0]
probabilities = model.predict_proba(new_student)[0]
print("\n========== NEW STUDENT ==========")
print("Study Hours:", new_student["Hours"].iloc[0])
print("Marks:", new_student["Marks"].iloc[0])
print("Predicted Result:", "Pass" if prediction == 1 else "Fail")
print(f"Fail Probability: {probabilities[0]:.2%}")
print(f"Pass Probability: {probabilities[1]:.2%}")
print("\n========== PROJECT COMPLETED ==========")