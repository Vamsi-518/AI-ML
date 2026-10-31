
import matplotlib.pyplot as plt
import seaborn as sns
from cluster_prediction import predict_clusters
def visualize_clusters():
    df = predict_clusters()
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="Annual_Income",
        y="Spending_Score",
        hue="Cluster",
        palette="viridis",
        s=100
    )
    plt.title("Customer Segmentation Using K-Means")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.legend(title="Cluster")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    visualize_clusters()
