from clustering_dataset import load_dataset
def select_features():
    df = load_dataset()
    features = df[
        ["Annual_Income", "Spending_Score"]
    ]
    print("\nSelected Features:")
    print(features.head())
    return features
if __name__ == "__main__":
    select_features()
