from dataset import load_dataset
def select_features():
    df = load_dataset()
    X = df.drop(columns=["target"])
    y = df["target"]
    print("\nSelected features:")
    print(X.head())
    return X, y
if __name__ == "__main__":
    select_features()