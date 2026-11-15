
import matplotlib.pyplot as plt

from sequence_dataset import load_sequence_dataset
from data_preprocessing import preprocess_data
from sequence_generation import create_train_test_sequences
from model_training import train_model
from prediction import make_predictions, actual_values
from model_evaluation import evaluate_model
def run_rnn_project():
    print("=" * 50)
    print("RNN AND LSTM TIME SERIES FORECASTING")
    print("=" * 50)
    # 1. Load dataset
    df = load_sequence_dataset()
    values = df["value"].values
    # 2. Preprocess data
    train_data, test_data, scaler = preprocess_data(values)
    # 3. Generate sequences
    X_train, y_train, X_test, y_test = (
        create_train_test_sequences(
            train_data,
            test_data,
            lookback=20
        )
    )
    actual = actual_values(y_test, scaler)
    results = {}
    # 4. Train and evaluate both models
    for model_type in ["SimpleRNN", "LSTM"]:
        print(f"\nTraining {model_type} model")
        model, history = train_model(
            X_train,
            y_train,
            model_type=model_type,
            epochs=20
        )
        # 5. Generate predictions
        predicted = make_predictions(
            model,
            X_test,
            scaler
        )
        # 6. Evaluate model
        metrics = evaluate_model(
            actual,
            predicted,
            model_type
        )
        results[model_type] = metrics
        # 7. Visualize actual and predicted values
        plt.figure(figsize=(10, 5))
        plt.plot(
            actual,
            label="Actual Values"
        )
        plt.plot(
            predicted,
            label=f"{model_type} Predictions"
        )
        plt.title(f"{model_type} Time Series Forecast")
        plt.xlabel("Time Steps")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        # 8. Visualize training loss
        plt.figure(figsize=(8, 4))
        plt.plot(
            history.history["loss"],
            label="Training Loss"
        )
        plt.plot(
            history.history["val_loss"],
            label="Validation Loss"
        )
        plt.title(f"{model_type} Training Loss")
        plt.xlabel("Epochs")
        plt.ylabel("Loss")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    print("\nMODEL COMPARISON")
    print("=" * 40)
    for model_type, metrics in results.items():
        print(f"\n{model_type}:")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")
    print("\nRNN project completed successfully!")
if __name__ == "__main__":
    run_rnn_project()


