import numpy as np
from softmax_function import softmax
def top_k_sampling(logits, k=3, seed=None):
    if k < 1 or k > len(logits):
        raise ValueError("K must be between 1 and vocabulary size.")
    top_indices = np.argsort(logits)[-k:]
    top_logits = logits[top_indices]
    probabilities = softmax(top_logits)
    rng = np.random.default_rng(seed)
    selected_position = int(
        rng.choice(
            len(top_indices),
            p=probabilities
        )
    )
    selected_token = int(
        top_indices[selected_position]
    )
    return selected_token
if __name__ == "__main__":
    logits = np.array([
        1.0,
        2.0,
        3.0,
        4.0,
        0.5
    ])
    result = top_k_sampling(
        logits,
        k=3,
        seed=42
    )
    print("Selected token:", result)