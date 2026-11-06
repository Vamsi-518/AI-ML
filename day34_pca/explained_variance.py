from pca_transformation import transform_data
def show_explained_variance():
    X_pca, pca = transform_data()
    print("\nExplained variance ratio:")
    for index, ratio in enumerate(
        pca.explained_variance_ratio_,
        start=1
    ):
        print(f"Principal Component {index}: {ratio:.4f}")
    total_variance = pca.explained_variance_ratio_.sum()
    print(f"\nTotal variance retained: {total_variance:.4f}")
    return pca.explained_variance_ratio_
if __name__ == "__main__":
    show_explained_variance()