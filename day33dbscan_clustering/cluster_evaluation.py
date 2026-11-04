from sklearn.metrics import silhouette_score
from model_training import train_model
def evaluate_clusters():
    model, X_scaled, scaler, labels = train_model()
    # DBSCAN labels noise points as -1
    non_noise_mask = labels != -1
    filtered_labels = labels[non_noise_mask]
    filtered_data = X_scaled[non_noise_mask]
    unique_clusters = set(filtered_labels)
    if len(unique_clusters) < 2:
        print(
            "Silhouette Score cannot be calculated: "
            "DBSCAN found fewer than two non-noise clusters."
        )
        return None
    score = silhouette_score(filtered_data, filtered_labels)
    noise_count = sum(labels == -1)
    print(f"\nSilhouette Score: {score:.4f}")
    print(f"Noise points: {noise_count}")
    return score
if __name__ == "__main__":
    evaluate_clusters()