import matplotlib.pyplot as plt
import seaborn as sns
from cluster_prediction import get_cluster_results
def visualize_clusters():
    df, X_scaled, cluster_labels = get_cluster_results()
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="Feature_1",
        y="Feature_2",
        hue="Cluster",
        palette="viridis",
        s=60
    )
    plt.title("DBSCAN Clustering")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend(title="Cluster")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    visualize_clusters()