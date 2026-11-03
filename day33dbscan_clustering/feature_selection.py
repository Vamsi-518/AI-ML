from clustering_dataset import load_dataset
def select_features():
    df = load_dataset()
    features = df[["Feature_1", "Feature_2"]]
    print("\nSelected features:")
    print(features.head())
    return features
if __name__ == "__main__":
    select_features()