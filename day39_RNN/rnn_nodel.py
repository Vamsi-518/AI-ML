
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, SimpleRNN, LSTM, Dense, Dropout
def build_recurrent_model(
    model_type="SimpleRNN",
    lookback=20
):
    tf.keras.utils.set_random_seed(42)
    model = Sequential()
    model.add(Input(shape=(lookback, 1)))
    if model_type == "SimpleRNN":
        model.add(
            SimpleRNN(50, activation="tanh")
        )
    elif model_type == "LSTM":
        model.add(
            LSTM(50, activation="tanh")
        )
    else:
        raise ValueError(
            "model_type must be SimpleRNN or LSTM"
        )
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(
        optimizer="adam",
        loss="mean_squared_error"
    )
    model.summary()
    return model
