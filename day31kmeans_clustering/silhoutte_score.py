
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from data_preprocessing import preprocess_data
def evaluate_silhouette():
    X_scaled, scaler = preprocess_data()
    for k in range(2, 8):
        model = KMeans(
            n_clusters=k,
            n_init=10,
            random_state=42
        )
        labels = model.fit_predict(X_scaled)
        score = silhouette_score(X_scaled, labels)
        print(
            f"K = {k}, Silhouette Score = {score:.4f}"
        )
if __name__ == "__main__":
    evaluate_silhouette()
