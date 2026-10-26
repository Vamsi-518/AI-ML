
from sklearn.datasets import load_iris
def load_dataset():
    iris = load_iris(as_frame=True)
    df = iris.data.copy()
    df["target"] = iris.target
    print("Dataset loaded successfully!")
    print("\nFirst five rows:")
    print(df.head())
    print("\nDataset shape:", df.shape)
    print("\nSpecies:", list(iris.target_names))
    return df
if __name__ == "__main__":
    load_dataset()
