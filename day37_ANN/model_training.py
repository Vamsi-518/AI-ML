
from neural_network_dataset import load_dataset
from feature_selection import select_features
from data_preprocessing import preprocess_data
from neural_network_model import build_model
def train_model():
    df = load_dataset()
    X, y = select_features(df)
    X_train, X_test, y_train, y_test, scaler = preprocess_data(X, y)
    model = build_model(
        input_dim=X_train.shape[1],
        num_classes=len(set(y))
    )
    history = model.fit(
        X_train,
        y_train,
        epochs=50,
        batch_size=8,
        validation_split=0.2,
        verbose=1
    )
    print("\nModel training completed!")
    return model, history, X_test, y_test, scaler
if __name__ == "__main__":
    train_model()
