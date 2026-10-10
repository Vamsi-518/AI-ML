from sklearn.model_selection import train_test_split
X = [
    [1, 20],
    [2, 30],
    [3, 40],
    [4, 50],
    [5, 60],
    [6, 70],
    [7, 80],
    [8, 90]
]
y = [0, 0, 0, 1, 1, 1, 1, 1]
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
print("\nTraining Targets:")
print(y_train)
print("\nTesting Targets:")
print(y_test)