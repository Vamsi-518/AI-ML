from sklearn.preprocessing import StandardScaler
from clustering_dataset import load_dataset
def preprocess_data():
    df = load_dataset()
    features = df[["Annual_Income", "Spending_Score"]]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    print("\nData preprocessing completed!")
    return scaled_features, scaler
if __name__ == "__main__":
    preprocess_data()