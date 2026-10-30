
from sklearn.preprocessing import StandardScaler
from clustering_dataset import load_dataset
def preprocess_data():
    df = load_dataset()
    X = df[["Annual_Income", "Spending_Score"]]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("\nData preprocessing completed!")
    print(X_scaled[:5])
    return X_scaled, scaler
if __name__ == "__main__":
    preprocess_data()
