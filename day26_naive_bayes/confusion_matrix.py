import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 6, 7],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 55, 85, 90],
    "Assignments": [20, 30, 40, 50, 65, 75, 85, 95, 35, 45, 80, 90],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)
display.plot()
plt.title("Naive Bayes Confusion Matrix")
plt.tight_layout()
plt.show()
print("Confusion Matrix:")
print(cm)
