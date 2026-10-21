
import pandas as pd
from sklearn.naive_bayes import GaussianNB
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 6, 7],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 55, 85, 90],
    "Assignments": [20, 30, 40, 50, 65, 75, 85, 95, 35, 45, 80, 90],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]
model = GaussianNB()
model.fit(X, y)
new_student = pd.DataFrame([{
    "Hours": 6,
    "Attendance": 85,
    "Assignments": 80
}])
prediction = model.predict(new_student)[0]
probabilities = model.predict_proba(new_student)[0]
label = "Pass" if prediction == 1 else "Fail"
print("New Student Details:")
print(new_student)
print("\nPredicted Result:", label)
print("Probability of Fail:", round(probabilities[0], 3))
print("Probability of Pass:", round(probabilities[1], 3))
