import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
def main():
    # Step 1: Create dataset
    data = {
        "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 6, 7],
        "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 55, 85, 90],
        "Assignments": [20, 30, 40, 50, 65, 75, 85, 95, 35, 45, 80, 90],
        "Result": [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
    }
    df = pd.DataFrame(data)
    # Step 2: Separate features and target
    X = df[["Hours", "Attendance", "Assignments"]]
    y = df["Result"]
    # Step 3: Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )
    # Step 4: Create and train the model
    model = GaussianNB()
    model.fit(X_train, y_train)
    # Step 5: Evaluate the model
    y_pred = model.predict(X_test)
    print("=" * 40)
    print("NAIVE BAYES CLASSIFICATION PROJECT")
    print("=" * 40)
    print(f"\nDataset size: {len(df)}")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.2%}")
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
    # Step 6: Predict for a new student
    new_student = pd.DataFrame([{
        "Hours": 6,
        "Attendance": 85,
        "Assignments": 80
    }])
    prediction = model.predict(new_student)[0]
    probabilities = model.predict_proba(new_student)[0]
    print("\nNew Student Prediction:")
    print(new_student.to_string(index=False))
    print("Predicted Result:", "Pass" if prediction == 1 else "Fail")
    print(f"Pass Probability: {probabilities[1]:.2%}")
    print(f"Fail Probability: {probabilities[0]:.2%}")
if __name__ == "__main__":
    main()
