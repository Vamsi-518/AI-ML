from sklearn.model_selection import train_test_split
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
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
print("Training Features:")
print(X_train)
print("\nTesting Features:")
print(X_test)
print("\nTraining Labels:")
print(y_train)
print("\nTesting Labels:")
print(y_test)