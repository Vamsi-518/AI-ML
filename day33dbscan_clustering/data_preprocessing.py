from sklearn.preprocessing import StandardScaler
from clustering_dataset import load_dataset
def preprocess_data():
    df = load_dataset()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    print("\nData preprocessing completed!")
    return X_scaled, scaler
if __name__ == "__main__":
    preprocess_data()