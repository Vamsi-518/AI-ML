import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Attendance"]]
y = df["Result"]
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)
new_student = pd.DataFrame({
    "Hours": [6],
    "Attendance": [85]
})
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)
print("Study Hours:", new_student["Hours"].iloc[0])
print("Attendance:", new_student["Attendance"].iloc[0])
if prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")
print("Class Probabilities:", probability[0])