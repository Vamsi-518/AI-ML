from model_training import train_model
from model_evaluation import evaluate_model
from loss_visualization import plot_training_history
def run_ann_project():
    print("=" * 50)
    print("ARTIFICIAL NEURAL NETWORK PROJECT")
    print("=" * 50)
    # Train model
    model, history, X_test, y_test, scaler = train_model()
    # Evaluate model
    evaluate_model(model, X_test, y_test)
    # Plot training history
    plot_training_history(history)
    print("\nANN project completed successfully!")
if __name__ == "__main__":
    run_ann_project()
