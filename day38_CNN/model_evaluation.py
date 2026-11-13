
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
def evaluate_cnn_model(model, X_test, y_test, class_names):
    probabilities = model.predict(X_test, verbose=0)
    predictions = np.argmax(probabilities, axis=1)
    accuracy = accuracy_score(y_test, predictions)
    print("\nCNN Model Accuracy:", accuracy)
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=class_names,
            zero_division=0
        )
    )
    return accuracy
if __name__ == "__main__":
    from model_training import train_cnn_model
    model, history, X_test, y_test, class_names = train_cnn_model()
    evaluate_cnn_model(model, X_test, y_test, class_names)
