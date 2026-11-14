
from sklearn.preprocessing import MinMaxScaler
def preprocess_data(values, train_ratio=0.8):
    split_index = int(len(values) * train_ratio)
    train_values = values[:split_index]
    test_values = values[split_index:]
    scaler = MinMaxScaler()
    train_scaled = scaler.fit_transform(
        train_values.reshape(-1, 1)
    ).flatten()
    test_scaled = scaler.transform(
        test_values.reshape(-1, 1)
    ).flatten()
    print("Preprocessing completed!")
    print("Training values:", len(train_scaled))
    print("Testing values:", len(test_scaled))
    return train_scaled, test_scaled, scaler
if __name__ == "__main__":
    from sequence_dataset import load_sequence_dataset
    df = load_sequence_dataset()
    train, test, scaler = preprocess_data(
        df["value"].values
    )
