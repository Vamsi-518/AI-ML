from sklearn.metrics import silhouette_score
from model_training import train_model
def evaluate_clusters():
    model, X_scaled, scaler, cluster_labels = train_model()
    score = silhouette_score(X_scaled, cluster_labels)
    print(f"\nSilhouette Score: {score:.4f}")
    return score
if __name__ == "__main__":
    evaluate_clusters()