import matplotlib.pyplot as plt
import seaborn as sns
from cluster_prediction import get_cluster_results
def visualize_clusters():
    df, X_scaled, cluster_labels = get_cluster_results()
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="Annual_Income",
        y="Spending_Score",
        hue="Cluster",
        palette="viridis",
        s=100
    )
    plt.title("Customer Groups — Hierarchical Clustering")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    visualize_clusters()