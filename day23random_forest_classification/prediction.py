import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95],
    "Assignments": [20, 30, 40, 50, 65, 75, 85, 95],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y)
new_student = pd.DataFrame({
    "Hours": [6],
    "Attendance": [85],
    "Assignments": [80]
})
prediction = model.predict(new_student)
probabilities = model.predict_proba(new_student)[0]
print("New Student Details:")
print(new_student)
print("\nPredicted Result:")
if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")
print("\nClass Probabilities:")
for label, probability in zip(model.classes_, probabilities):
    print(f"Class {label}: {probability:.2%}")