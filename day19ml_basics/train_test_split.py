#Divide data into training and testing data.

from sklearn.model_selection import train_test_split
X = [[1], [2], [3], [4], [5], [6]]
y = [35, 45, 50, 60, 70, 80]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("Training Features:")
print(X_train)
print("\nTesting Features:")
print(X_test)
print("\nTraining Target:")
print(y_train)
print("\nTesting Target:")
print(y_test)