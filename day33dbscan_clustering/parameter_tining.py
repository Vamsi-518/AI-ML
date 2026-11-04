import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from data_preprocessing import preprocess_data
def plot_k_distance(min_samples=5):
    X_scaled, scaler = preprocess_data()
    neighbors = NearestNeighbors(n_neighbors=min_samples)
    neighbors.fit(X_scaled)
    distances, indices = neighbors.kneighbors(X_scaled)
    # Distance to the kth nearest neighbor
    k_distances = sorted(distances[:, -1])
    plt.figure(figsize=(9, 5))
    plt.plot(k_distances)
    plt.title("DBSCAN K-Distance Plot")
    plt.xlabel("Points sorted by distance")
    plt.ylabel(f"Distance to {min_samples}th nearest neighbor")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    plot_k_distance()