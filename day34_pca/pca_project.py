from sklearn.decomposition import PCA
from dataset import load_dataset
from data_preprocessing import preprocess_data
from pca_visualization import visualize_pca
def run_project():
    # Load dataset
    df = load_dataset()
    # Standardize features
    X_scaled, scaler = preprocess_data()
    # Fit PCA and reduce to two components
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    print("\nPCA completed!")
    print("Original data shape:", X_scaled.shape)
    print("Reduced data shape:", X_pca.shape)
    print(
        "\nVariance retained:",
        round(pca.explained_variance_ratio_.sum(), 4)
    )
    print("\nExplained variance by component:")
    print(pca.explained_variance_ratio_)
    # Visualize the reduced data
    visualize_pca()
    print("\nDay 34 PCA project completed!")
if __name__ == "__main__":
    run_project()