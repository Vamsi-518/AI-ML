import numpy as np
from softmax_function import softmax
def temperature_sampling(
    logits,
    temperature=1.0,
    seed=None
):
    probabilities = softmax(
        logits,
        temperature
    )
    rng = np.random.default_rng(seed)
    selected_token = int(
        rng.choice(
            len(probabilities),
            p=probabilities
        )
    )
    return selected_token, probabilities
if __name__ == "__main__":
    logits = np.array([2.0, 1.0, 0.5, 3.0])
    token, probabilities = temperature_sampling(
        logits,
        temperature=0.7,
        seed=42
    )
    print("Probabilities:", probabilities)
    print("Selected token:", token)