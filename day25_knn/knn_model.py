
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
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
    KNeighborsClassifier(n_neighbors=3)
)
model.fit(X, y)
print("KNN model trained successfully!")
print("Number of neighbors:", 3)
print("Classes:", model.named_steps["kneighborsclassifier"].classes_)
print("\nTraining predictions:")
print(model.predict(X))
