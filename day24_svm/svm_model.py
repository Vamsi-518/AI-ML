from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
X = [
    [1, 40, 20],
    [2, 45, 30],
    [3, 50, 40],
    [4, 60, 50],
    [5, 70, 65],
    [6, 80, 75],
    [7, 90, 85],
    [8, 95, 95]
]
y = [0, 0, 0, 0, 1, 1, 1, 1]
model = make_pipeline(
    StandardScaler(),
    SVC(kernel="linear", C=1.0)
)
model.fit(X, y)
print("SVM model trained successfully!")
print("Kernel:", model.named_steps["svc"].kernel)
print("Classes:", model.named_steps["svc"].classes_)
predictions = model.predict(X)
print("Training predictions:", predictions)
