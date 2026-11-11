
import matplotlib.pyplot as plt
def plot_training_history(history):
    plt.figure(figsize=(8, 5))
    plt.plot(
        history.history["loss"],
        label="Training Loss"
    )
    plt.plot(
        history.history["val_loss"],
        label="Validation Loss"
    )
    plt.title("ANN Training and Validation Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    from model_training import train_model
    model, history, X_test, y_test, scaler = train_model()
    plot_training_history(history)
