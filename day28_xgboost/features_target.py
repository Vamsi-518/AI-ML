
from classification_dataset import load_dataset
def get_features_target():
    df = load_dataset()
    X = df.drop("target", axis=1)
    y = df["target"]
    print("\nFeatures:")
    print(X.head())
    print("\nTarget:")
    print(y.head())
    return X, y
if __name__ == "__main__":
    get_features_target()
