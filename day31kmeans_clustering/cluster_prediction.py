from model_training import train_model
from clustering_dataset import load_dataset
def predict_clusters():
    model, X_scaled, scaler = train_model()
    df = load_dataset()
    clusters = model.predict(X_scaled)
    df["Cluster"] = clusters
    print("\nCustomer Cluster Predictions:")
    print(df)
    print("\nCustomers in each cluster:")
    print(df["Cluster"].value_counts().sort_index())
    return df
if __name__ == "__main__":
    predict_clusters()
