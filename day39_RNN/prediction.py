
def make_predictions(model, X_test, scaler):
    predictions_scaled = model.predict(
        X_test,
        verbose=0
    )
    predictions = scaler.inverse_transform(
        predictions_scaled
    ).flatten()
    print("Predicted values:")
    print(predictions[:10])
    return predictions
def actual_values(y_test, scaler):
    return scaler.inverse_transform(
        y_test.reshape(-1, 1)
    ).flatten()
