
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Sample numerical data
X = np.array([
    [1, 40],
    [2, 45],
    [3, 50],
    [4, 60],
    [5, 70],
    [6, 80],
    [7, 90],
    [8, 95]
])

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

model = GaussianNB()
model.fit(X, y)

# Predict for a new student: 6 hours, 85% attendance
new_student = np.array([[6, 85]])

prediction = model.predict(new_student)[0]
probability = model.predict_proba(new_student)[0]

print("Gaussian Naive Bayes Demonstration")
print("Predicted Result:", "Pass" if prediction == 1 else "Fail")
print("Class Probabilities:", model.classes_)
print("Probabilities:", np.round(probability, 3))

training_predictions = model.predict(X)
print(
    "Training Accuracy:",
    f"{accuracy_score(y, training_predictions):.2%}"
)
