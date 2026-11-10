
import pandas as pd
from sklearn.datasets import load_iris
def load_dataset():
    iris = load_iris()
    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )
    df["target"] = iris.target
    print("Dataset loaded successfully!")
    print(df.head())
    return df
if __name__ == "__main__":
    dataset = load_dataset()
    print("\nDataset shape:", dataset.shape)
