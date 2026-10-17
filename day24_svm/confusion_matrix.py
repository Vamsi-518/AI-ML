import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
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
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
model = make_pipeline(
    StandardScaler(),
    SVC(kernel="rbf", C=1.0)
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
print("Confusion Matrix:")
print(cm)
print("Labels: 0 = Fail, 1 = Pass")
print("Rows = Actual, Columns = Predicted")
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)
display.plot()
plt.title("SVM Confusion Matrix")
plt.tight_layout()
plt.show()
