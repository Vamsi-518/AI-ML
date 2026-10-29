
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from train_test_split import split_dataset
def tune_model():
    X_train, X_test, y_train, y_test = split_dataset()
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=3000))
    ])
    parameters = {
        "classifier__C": [0.01, 0.1, 1, 10, 100],
        "classifier__class_weight": [None, "balanced"]
    }
    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )
    search = GridSearchCV(
        pipeline,
        parameters,
        cv=cv,
        scoring="accuracy",
        n_jobs=-1
    )
    search.fit(X_train, y_train)
    print("\nBest parameters:")
    print(search.best_params_)
    print("\nBest cross-validation accuracy:")
    print(round(search.best_score_ * 100, 2), "%")
    print("\nTest accuracy of selected model:")
    print(round(search.score(X_test, y_test) * 100, 2), "%")
    return search.best_estimator_
if __name__ == "__main__":
    tune_model()
