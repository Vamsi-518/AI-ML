import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import silhouette_score
from clustering_dataset import load_dataset
from data_preprocessing import preprocess_data
from hierarchical_model import create_model
def run_project():
    # Load data
    df = load_dataset()
    # Scale features
    X_scaled, scaler = preprocess_data()
    # Train hierarchical clustering model
    model = create_model(n_clusters=3, linkage="ward")
    cluster_labels = model.fit_predict(X_scaled)
    # Add cluster labels to the dataset
    df["Cluster"] = cluster_labels
    print("\nCluster assignments:")
    print(df)
    # Evaluate clusters
    score = silhouette_score(X_scaled, cluster_labels)
    print(f"\nSilhouette Score: {score:.4f}")
    # Plot dendrogram
    linked_data = linkage(X_scaled, method="ward")
    plt.figure(figsize=(10, 6))
    dendrogram(linked_data)
    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Data Points")
    plt.ylabel("Distance")
    plt.tight_layout()
    plt.show()
    # Plot clusters
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="Annual_Income",
        y="Spending_Score",
        hue="Cluster",
        palette="viridis",
        s=100
    )
    plt.title("Customer Segmentation")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.tight_layout()
    plt.show()
    print("\nHierarchical Clustering Project Completed!")
if __name__ == "__main__":
    run_project()