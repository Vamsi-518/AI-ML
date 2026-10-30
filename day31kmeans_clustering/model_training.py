
from data_preprocessing import preprocess_data
from kmeans_model import create_model
def train_model():
    X_scaled, scaler = preprocess_data()
    model = create_model(n_clusters=3)
    model.fit(X_scaled)
    print("\nK-Means model trained successfully!")
    print("\nCluster Centers:")
    print(model.cluster_centers_)
    return model, X_scaled, scaler
if __name__ == "__main__":
    train_model()
