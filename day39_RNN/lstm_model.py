
from rnn_model import build_recurrent_model
def create_lstm_model(lookback=20):
    model = build_recurrent_model(
        model_type="LSTM",
        lookback=lookback
    )
    return model
if __name__ == "__main__":
    model = create_lstm_model()
