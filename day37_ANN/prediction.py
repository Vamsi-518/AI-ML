import numpy as np
def make_predictions(model, X_test):
    probabilities = model.predict(X_test, verbose=0)
    predictions = np.argmax(probabilities, axis=1)
    print("Predicted classes:")
    print(predictions[:10])
    return predictions
if __name__ == "__main__":
    from model_training import train_model
    model, history, X_test, y_test, scaler = train_model()
    predictions = make_predictions(model, X_test)
