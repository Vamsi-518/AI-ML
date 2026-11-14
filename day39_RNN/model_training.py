
from rnn_model import build_recurrent_model
def train_model(
    X_train,
    y_train,
    model_type="SimpleRNN",
    epochs=20
):
    model = build_recurrent_model(
        model_type=model_type,
        lookback=X_train.shape[1]
    )
    history = model.fit(
        X_train,
        y_train,
        epochs=epochs,
        batch_size=32,
        validation_split=0.2,
        shuffle=False,
        verbose=1
    )
    print(model_type, "training completed!")
    return model, history
if __name__ == "__main__":
    from sequence_dataset import load_sequence_dataset
    from data_preprocessing import preprocess_data
    from sequence_generation import create_sequences
    df = load_sequence_dataset()
    train, test, scaler = preprocess_data(
        df["value"].values
    )
    X_train, y_train = create_sequences(train)
    model, history = train_model(
        X_train,
        y_train
    )
