
from xgboost import XGBClassifier
def create_model():
    model = XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        objective="multi:softprob",
        eval_metric="mlogloss",
        random_state=42
    )
    print("XGBoost model created successfully!")
    return model
if __name__ == "__main__":
    create_model()
