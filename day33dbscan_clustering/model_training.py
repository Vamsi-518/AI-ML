from data_preprocessing import preprocess_data
from dbscan_model import create_model
def train_model(eps=0.25, min_samples=5):
    X_scaled, scaler = preprocess_data()
    model = create_model(
        eps=eps,
        min_samples=min_samples
    )
    cluster_labels = model.fit_predict(X_scaled)
    print("\nDBSCAN clustering completed!")
    return model, X_scaled, scaler, cluster_labels
if __name__ == "__main__":
    train_model()