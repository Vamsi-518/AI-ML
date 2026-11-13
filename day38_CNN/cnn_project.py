
from model_training import train_cnn_model
from prediction import predict_image
from model_evaluation import evaluate_cnn_model
from accuracy_visualization import plot_accuracy
def run_cnn_project():
    print("=" * 50)
    print("CONVOLUTIONAL NEURAL NETWORK PROJECT")
    print("=" * 50)
    # Train CNN model
    model, history, X_test, y_test, class_names = (
        train_cnn_model(epochs=10)
    )
    # Predict one test image
    print("\nImage Prediction:")
    predict_image(model, X_test[0], class_names)
    # Evaluate model
    print("\nModel Evaluation:")
    evaluate_cnn_model(
        model,
        X_test,
        y_test,
        class_names
    )
    # Visualize accuracy
    plot_accuracy(history)
    print("\nCNN project completed successfully!")
if __name__ == "__main__":
    run_cnn_project()
