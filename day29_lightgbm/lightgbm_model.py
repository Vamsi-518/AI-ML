
from lightgbm import LGBMClassifier
def create_model():
    model = LGBMClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=-1,
        num_leaves=15,
        objective="multiclass",
        random_state=42,
        verbosity=-1
    )
    print("LightGBM model created successfully!")
    return model
if __name__ == "__main__":
    create_model()