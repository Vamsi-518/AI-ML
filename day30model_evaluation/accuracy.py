
from sklearn.metrics import accuracy_score
from model_training import train_model
def calculate_accuracy():
    model, X_train, X_test, y_train, y_test = train_model()
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print("\nAccuracy:", round(accuracy * 100, 2), "%")
    return accuracy
if __name__ == "__main__":
    calculate_accuracy()
