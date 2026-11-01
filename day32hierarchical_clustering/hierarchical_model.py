from sklearn.cluster import AgglomerativeClustering
def create_model(n_clusters=3, linkage="ward"):
    model = AgglomerativeClustering(
        n_clusters=n_clusters,
        linkage=linkage
    )
    print("Hierarchical clustering model created!")
    return model
if __name__ == "__main__":
    create_model()