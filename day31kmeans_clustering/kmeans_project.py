
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from clustering_dataset import load_dataset
from data_preprocessing import preprocess_data
from kmeans_model import create_model
def run_project():
    # 1. Load dataset
    df = load_dataset()
    # 2. Preprocess dataset
    X_scaled, scaler = preprocess_data()
    # 3. Create model
    model = create_model(n_clusters=3)
    # 4. Train model
    model.fit(X_scaled)
    print("\nModel training completed!")
    # 5. Predict clusters
    clusters = model.predict(X_scaled)
    df["Cluster"] = clusters
    print("\nCluster Results:")
    print(df)
    # 6. Evaluate clustering
    score = silhouette_score(X_scaled, clusters)
    print("\nSilhouette Score:", round(score, 4))
    print("\nCluster Distribution:")
    print(df["Cluster"].value_counts().sort_index())
    # 7. Visualize clusters
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="Annual_Income",
        y="Spending_Score",
        hue="Cluster",
        palette="viridis",
        s=100
    )
    plt.title("K-Means Customer Segmentation")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.tight_layout()
    plt.show()
    # 8. Display cluster centers in original scale
    centers = scaler.inverse_transform(
        model.cluster_centers_
    )
    print("\nCluster Centers (Original Scale):")
    print(centers)
    print("\nK-Means Project Completed!")
if __name__ == "__main__":
    run_project()
