import pandas as pd
from sklearn.linear_model import LogisticRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 30, 40, 50, 60, 70, 80, 90],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Marks"]]
y = df["Result"]
model = LogisticRegression()
model.fit(X, y)
new_student = pd.DataFrame({
    "Hours": [6],
    "Marks": [75]
})
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)
print("Study Hours:", new_student["Hours"].iloc[0])
print("Marks:", new_student["Marks"].iloc[0])
if prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")
print("Probability for Fail:", probability[0][0])
print("Probability for Pass:", probability[0][1])