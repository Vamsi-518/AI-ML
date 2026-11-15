
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)
def evaluate_model(actual, predicted, model_name):
    mae = mean_absolute_error(actual, predicted)
    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    print(f"\n{model_name} Evaluation")
    print("-" * 30)
    print(f"MAE:  {mae:.4f}")
    print(f"MSE:  {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse
    }
