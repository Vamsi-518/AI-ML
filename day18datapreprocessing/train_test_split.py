from sklearn.model_selection import train_test_split
X = [
    [20, 60],
    [21, 65],
    [22, 70],
    [23, 75],
    [24, 80],
    [25, 85]
]
y = [0, 0, 0, 1, 1, 1]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("Training Data:")
print(X_train)
print("\nTesting Data:")
print(X_test)
print("\nTraining Labels:")
print(y_train)
print("\nTesting Labels:")
print(y_test)