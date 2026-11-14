
import numpy as np
def create_sequences(data, lookback=20):
    X = []
    y = []
    for i in range(lookback, len(data)):
        X.append(data[i - lookback:i])
        y.append(data[i])
    X = np.array(X)
    y = np.array(y)
    X = X.reshape(X.shape[0], X.shape[1], 1)
    print("Sequences created!")
    print("Input shape:", X.shape)
    print("Output shape:", y.shape)
    return X, y
def create_train_test_sequences(
    train_data,
    test_data,
    lookback=20
):
    X_train, y_train = create_sequences(
        train_data,
        lookback
    )
    # Include the final training observations as context
    # for the first test sequence.
    combined = np.concatenate([
        train_data[-lookback:],
        test_data
    ])
    X_test, y_test = create_sequences(
        combined,
        lookback
    )
    return X_train, y_train, X_test, y_test
if __name__ == "__main__":
    sample_data = np.arange(100, dtype=float)
    X, y = create_sequences(sample_data)
    print("First input sequence:", X[0].flatten())
    print("First target:", y[0])
