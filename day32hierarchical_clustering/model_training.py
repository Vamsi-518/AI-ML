from data_preprocessing import preprocess_data
from hierarchical_model import create_model
def train_model(n_clusters=3):
    X_scaled, scaler = preprocess_data()
    model = create_model(n_clusters=n_clusters)
    cluster_labels = model.fit_predict(X_scaled)
    print("\nModel training completed!")
    return model, X_scaled, scaler, cluster_labels
if __name__ == "__main__":
    train_model()