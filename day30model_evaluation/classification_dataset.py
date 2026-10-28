
from sklearn.datasets import load_breast_cancer
def load_dataset():
    dataset = load_breast_cancer(as_frame=True)
    df = dataset.data.copy()
    df["target"] = dataset.target
    print("Dataset loaded successfully!")
    print("\nFirst five rows:")
    print(df.head())
    print("\nDataset shape:", df.shape)
    print("\nTarget classes:", list(dataset.target_names))
    return df
if __name__ == "__main__":
    load_dataset()
