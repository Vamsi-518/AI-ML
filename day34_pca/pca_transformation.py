from data_preprocessing import preprocess_data
from pca_model import create_pca_model
def transform_data(n_components=2):
    X_scaled, scaler = preprocess_data()
    pca = create_pca_model(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    print("\nPCA transformation completed!")
    print("Transformed data shape:", X_pca.shape)
    return X_pca, pca
if __name__ == "__main__":
    transform_data()