
from sklearn.cluster import KMeans
def create_model(n_clusters=3):
    model = KMeans(
        n_clusters=n_clusters,
        init="k-means++",
        n_init=10,
        random_state=42
    )
    print("K-Means model created successfully!")
    return model
if __name__ == "__main__":
    create_model()
