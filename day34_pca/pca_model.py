from sklearn.decomposition import PCA
def create_pca_model(n_components=2):
    pca = PCA(n_components=n_components)
    print("PCA model created!")
    return pca
if __name__ == "__main__":
    create_pca_model()