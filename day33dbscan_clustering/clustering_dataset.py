import pandas as pd
from sklearn.datasets import make_moons
def load_dataset():
    # Generate sample data with curved clusters
    features, _ = make_moons(
        n_samples=300,
        noise=0.08,
        random_state=42
    )
    df = pd.DataFrame(
        features,
        columns=["Feature_1", "Feature_2"]
    )
    print("Dataset loaded successfully!")
    print(df.head())
    return df
if __name__ == "__main__":
    load_dataset()