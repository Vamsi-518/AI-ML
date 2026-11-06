import pandas as pd
from dataset import load_dataset
from pca_transformation import transform_data
def reduce_dimensions():
    df = load_dataset()
    X_pca, pca = transform_data(n_components=2)
    reduced_df = pd.DataFrame(
        X_pca,
        columns=["Principal_Component_1", "Principal_Component_2"]
    )
    reduced_df["target"] = df["target"]
    print("\nReduced dataset:")
    print(reduced_df.head())
    print("\nOriginal feature count:", 4)
    print("Reduced feature count:", X_pca.shape[1])
    return reduced_df
if __name__ == "__main__":
    reduce_dimensions()