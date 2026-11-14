
import numpy as np
import pandas as pd
def load_sequence_dataset():
    np.random.seed(42)
    time = np.arange(1000)
    trend = 0.01 * time
    seasonal = np.sin(0.05 * time)
    noise = np.random.normal(0, 0.1, len(time))
    values = trend + seasonal + noise
    df = pd.DataFrame({
        "time": time,
        "value": values
    })
    print("Time-series dataset created!")
    print(df.head())
    return df
if __name__ == "__main__":
    dataset = load_sequence_dataset()
    print("\nDataset shape:", dataset.shape)
