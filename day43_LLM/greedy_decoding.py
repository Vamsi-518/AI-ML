import numpy as np
def greedy_decoding(probabilities):
    predicted_token = int(
        np.argmax(probabilities)
    )
    return predicted_token
if __name__ == "__main__":
    probabilities = np.array([
        0.10,
        0.20,
        0.60,
        0.10
    ])
    result = greedy_decoding(probabilities)
    print("Predicted token ID:", result)