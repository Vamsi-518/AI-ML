
import matplotlib.pyplot as plt
def plot_accuracy(history):
    plt.figure(figsize=(8, 5))
    plt.plot(
        history.history["accuracy"],
        label="Training Accuracy"
    )
    plt.plot(
        history.history["val_accuracy"],
        label="Validation Accuracy"
    )
    plt.title("CNN Training and Validation Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    from model_training import train_cnn_model
    model, history, X_test, y_test, class_names = train_cnn_model()
    plot_accuracy(history)
