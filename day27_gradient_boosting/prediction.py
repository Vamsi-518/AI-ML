
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 6, 7],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 55, 85, 90],
    "Assignments": [20, 30, 40, 50, 65, 75, 85, 95, 35, 45, 80, 90],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]
model = GradientBoostingClassifier(random_state=42)
model.fit(X, y)
new_student = pd.DataFrame([{
    "Hours": 6,
    "Attendance": 85,
    "Assignments": 80
}])
prediction = model.predict(new_student)[0]
probabilities = model.predict_proba(new_student)[0]
print("New Student:")
print(new_student.to_string(index=False))
print("\nPredicted Result:", "Pass" if prediction == 1 else "Fail")
print(f"Fail Probability: {probabilities[0]:.2%}")
print(f"Pass Probability: {probabilities[1]:.2%}")
