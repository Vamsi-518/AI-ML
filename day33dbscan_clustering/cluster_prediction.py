from clustering_dataset import load_dataset
from model_training import train_model


def get_cluster_results():
    df = load_dataset()

    model, X_scaled, scaler, cluster_labels = train_model()

    df["Cluster"] = cluster_labels

    print("\nCluster assignments:")
    print(df)

    print("\nCluster counts:")
    print(df["Cluster"].value_counts().sort_index())

    return df, X_scaled, cluster_labels


if __name__ == "__main__":
    get_cluster_results()