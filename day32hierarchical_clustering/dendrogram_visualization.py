import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from data_preprocessing import preprocess_data
def plot_dendrogram():
    X_scaled, scaler = preprocess_data()
    linked_data = linkage(X_scaled, method="ward")
    plt.figure(figsize=(10, 6))
    dendrogram(
        linked_data,
        labels=[str(i) for i in range(1, len(X_scaled) + 1)]
    )
    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Customer")
    plt.ylabel("Distance")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    plot_dendrogram()