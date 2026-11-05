from sklearn.preprocessing import StandardScaler
from dataset import load_dataset
def preprocess_data():
    df = load_dataset()
    X = df.drop(columns=["target"])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("\nFeature scaling completed!")
    return X_scaled, scaler
if __name__ == "__main__":
    preprocess_data()