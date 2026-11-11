
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
from prediction import make_predictions
def evaluate_model(model, X_test, y_test):
    predictions = make_predictions(model, X_test)
    accuracy = accuracy_score(y_test, predictions)
    print("\nModel Accuracy:", accuracy)
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=[
                "Setosa",
                "Versicolor",
                "Virginica"
            ],
            zero_division=0
        )
    )
    return accuracy
if __name__ == "__main__":
    from model_training import train_model
    model, history, X_test, y_test, scaler = train_model()
    evaluate_model(model, X_test, y_test)
