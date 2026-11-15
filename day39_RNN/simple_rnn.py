
from rnn_model import build_recurrent_model
def create_simple_rnn(lookback=20):
    model = build_recurrent_model(
        model_type="SimpleRNN",
        lookback=lookback
    )
    return model
if __name__ == "__main__":
    model = create_simple_rnn()
