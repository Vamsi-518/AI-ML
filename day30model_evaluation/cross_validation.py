
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from features_target import get_features_target
def evaluate_cross_validation():
    X, y = get_features_target()
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])
    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )
    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )
    print("\nCross-validation scores:")
    print(scores)
    print("Mean accuracy:", round(scores.mean() * 100, 2), "%")
    print("Standard deviation:", round(scores.std(), 4))
if __name__ == "__main__":
    evaluate_cross_validation()
