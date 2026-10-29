
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    classification_report
)
from model_training import train_model
def evaluate_metrics():
    model, X_train, X_test, y_train, y_test = train_model()

    predictions = model.predict(X_test)
    print("\nPrecision:", round(
        precision_score(y_test, predictions, pos_label=0), 4
    ))
    print("Recall:", round(
        recall_score(y_test, predictions, pos_label=0), 4
    ))
    print("F1-score:", round(
        f1_score(y_test, predictions, pos_label=0), 4
    ))
    print("\nClassification Report:")
    print(classification_report(
        y_test,
        predictions,
        target_names=["malignant", "benign"]
    ))
if __name__ == "__main__":
    evaluate_metrics()
