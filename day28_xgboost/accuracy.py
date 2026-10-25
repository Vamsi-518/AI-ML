
from sklearn.metrics import accuracy_score
from prediction import make_predictions


def calculate_accuracy():
    y_test, predictions = make_predictions()

    accuracy = accuracy_score(y_test, predictions)

    print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

    return accuracy


if __name__ == "__main__":
    calculate_accuracy()
