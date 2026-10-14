from sklearn.ensemble import RandomForestClassifier
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
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=4,
    random_state=42
)
model.fit(X, y)
print("Random Forest model created and trained!")
print("Number of Trees:", len(model.estimators_))
print("Classes:", model.classes_)