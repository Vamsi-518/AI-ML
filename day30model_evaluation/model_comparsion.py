
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from features_target import get_features_target

def compare_models():
    X, y = get_features_target()
    models = {
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=2000))
        ]),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42
        )
    }
    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )
    results = {}
    print("\nModel Comparison")
    for name, model in models.items():
        scores = cross_val_score(
            model,
            X,
            y,
            cv=cv,
            scoring="accuracy"
        )
        results[name] = scores.mean()
        print(f"\n{name}")
        print("Fold scores:", scores.round(4))
        print("Mean accuracy:", round(scores.mean() * 100, 2), "%")
    best_model = max(results, key=results.get)
    print("\nBest model by mean cross-validation accuracy:")
    print(best_model)
    return results
if __name__ == "__main__":
    compare_models()
