
from classification_dataset import load_dataset
def get_features_target():
    df = load_dataset()
    X = df.drop("target", axis=1)
    y = df["target"]
    print("\nFeature shape:", X.shape)
    print("Target shape:", y.shape)
    return X, y
if __name__ == "__main__":
    get_features_target()
