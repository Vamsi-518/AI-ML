
import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix as calculate_matrix,
    ConfusionMatrixDisplay
)
from model_training import train_model
def display_confusion_matrix():
    model, X_train, X_test, y_train, y_test = train_model()
    predictions = model.predict(X_test)
    matrix = calculate_matrix(
        y_test,
        predictions,
        labels=[0, 1]
    )
    print("\nConfusion Matrix:")
    print(matrix)
    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=["malignant", "benign"]
    )
    display.plot()
    plt.title("Model Confusion Matrix")
    plt.tight_layout()
    plt.show()
    return matrix
if __name__ == "__main__":
    display_confusion_matrix()
