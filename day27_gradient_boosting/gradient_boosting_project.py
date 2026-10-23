
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
def main():
    # 1. Create dataset
    data = {
        "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 6, 7],
        "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 55, 85, 90],
        "Assignments": [20, 30, 40, 50, 65, 75, 85, 95, 35, 45, 80, 90],
        "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
    }
    df = pd.DataFrame(data)
    # 2. Separate features and target
    X = df[["Hours", "Attendance", "Assignments"]]
    y = df["Result"]
    # 3. Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )
    # 4. Create and train model
    model = GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )
    model.fit(X_train, y_train)
    # 5. Evaluate model
    y_pred = model.predict(X_test)
    print("=" * 45)
    print("GRADIENT BOOSTING CLASSIFICATION PROJECT")
    print("=" * 45)
    print("\nDataset size:", len(df))
    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred, labels=[0, 1]))
    print("\nClassification Report:")
    print(classification_report(
        y_test,
        y_pred,
        labels=[0, 1],
        target_names=["Fail", "Pass"],
        zero_division=0
    ))
    # 6. Plot confusion matrix
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred,
        labels=[0, 1],
        display_labels=["Fail", "Pass"]
    )
    plt.title("Gradient Boosting Confusion Matrix")
    plt.tight_layout()
    plt.show()
    # 7. Display feature importance
    importance = pd.Series(
        model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)
    print("\nFeature Importance:")
    print(importance)
    importance.plot(kind="bar")
    plt.title("Feature Importance")
    plt.ylabel("Importance")
    plt.tight_layout()
    plt.show()
    # 8. Predict for a new student
    new_student = pd.DataFrame([{
        "Hours": 6,
        "Attendance": 85,
        "Assignments": 80
    }])
    prediction = model.predict(new_student)[0]
    probabilities = model.predict_proba(new_student)[0]
    print("\nNew Student Details:")
    print(new_student.to_string(index=False))
    print("\nPredicted Result:", "Pass" if prediction == 1 else "Fail")
    print(f"Fail Probability: {probabilities[0]:.2%}")
    print(f"Pass Probability: {probabilities[1]:.2%}")
if __name__ == "__main__":
    main()
