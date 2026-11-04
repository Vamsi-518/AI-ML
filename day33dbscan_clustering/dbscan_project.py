import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score
from clustering_dataset import load_dataset
from data_preprocessing import preprocess_data
from dbscan_model import create_model
def run_project():
    # 1. Load dataset
    df = load_dataset()
    # 2. Preprocess features
    X_scaled, scaler = preprocess_data()
    # 3. Create and train DBSCAN
    model = create_model(eps=0.25, min_samples=5)
    cluster_labels = model.fit_predict(X_scaled)
    # 4. Display cluster assignments
    df["Cluster"] = cluster_labels
    print("\nCluster assignments:")
    print(df)
    print("\nCluster counts:")
    print(df["Cluster"].value_counts().sort_index())
    # 5. Evaluate clusters, excluding noise
    non_noise_mask = cluster_labels != -1
    filtered_labels = cluster_labels[non_noise_mask]
    filtered_data = X_scaled[non_noise_mask]
    if len(set(filtered_labels)) >= 2:
        score = silhouette_score(filtered_data, filtered_labels)
        print(f"\nSilhouette Score: {score:.4f}")
    else:
        print("\nSilhouette Score unavailable: fewer than two clusters.")
    # 6. Visualize clusters and noise
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="Feature_1",
        y="Feature_2",
        hue="Cluster",
        palette="viridis",
        s=60
    )
    plt.title("DBSCAN Clustering Results")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.tight_layout()
    plt.show()
    print("\nDBSCAN project completed!")
if __name__ == "__main__":
    run_project()