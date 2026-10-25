
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
from sklearn.datasets import load_iris

from train_test_split import split_dataset
from xgboost_model import create_model


def run_project():
    # 1. Load and split dataset
    X_train, X_test, y_train, y_test = split_dataset()

    # 2. Create and train model
    model = create_model()
    model.fit(X_train, y_train)

    print("\nModel training completed!")

    # 3. Make predictions
    predictions = model.predict(X_test)

    # 4. Evaluate accuracy
    accuracy = accuracy_score(y_test, predictions)
    print("\nAccuracy:", round(accuracy * 100, 2), "%")

    # 5. Classification report
    iris = load_iris()
    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            labels=[0, 1, 2],
            target_names=iris.target_names,
            zero_division=0
        )
    )

    # 6. Confusion matrix
    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=[0, 1, 2]
    )

    print("\nConfusion Matrix:")
    print(matrix)

    ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=iris.target_names
    ).plot()

    plt.title("XGBoost Confusion Matrix")
    plt.tight_layout()
    plt.show()

    # 7. Feature importance
    importance = pd.Series(
        model.feature_importances_,
        index=X_train.columns
    ).sort_values(ascending=False)

    print("\nFeature Importance:")
    print(importance)

    importance.sort_values().plot(
        kind="barh",
        title="XGBoost Feature Importance"
    )

    plt.xlabel("Importance Score")
    plt.tight_layout()
    plt.show()

    # 8. Predict one sample
    sample = X_test.iloc[[0]]
    prediction = int(model.predict(sample)[0])

    print("\nSample measurements:")
    print(sample)

    print(
        "Predicted flower species:",
        iris.target_names[prediction]
    )


if __name__ == "__main__":
    run_project()
