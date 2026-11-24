import numpy as np
def softmax(logits, temperature=1.0):
    if temperature <= 0:
        raise ValueError("Temperature must be positive.")
    scaled_logits = logits / temperature
    scaled_logits = (
        scaled_logits - np.max(scaled_logits)
    )
    exp_values = np.exp(scaled_logits)
    probabilities = (
        exp_values / np.sum(exp_values)
    )
    return probabilities
if __name__ == "__main__":
    scores = np.array([2.0, 1.0, 0.5, 3.0])
    probabilities = softmax(scores)
    print("Original scores:", scores)
    print("Probabilities:", probabilities)
    print("Probability sum:", probabilities.sum())