
def select_features(df):
    X = df.drop("target", axis=1)
    y = df["target"]
    print("Features selected:")
    print(X.head())
    print("\nTarget labels:")
    print(y.head())
    return X, y
if __name__ == "__main__":
    from neural_network_dataset import load_dataset
    dataset = load_dataset()
    X, y = select_features(dataset)
    print("\nFeature shape:", X.shape)
    print("Target shape:", y.shape)
