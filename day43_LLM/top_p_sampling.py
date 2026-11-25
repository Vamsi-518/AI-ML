import numpy as np
from softmax_function import softmax
def top_p_sampling(
    logits,
    p=0.9,
    seed=None
):
    if not 0 < p <= 1:
        raise ValueError("P must be greater than 0 and at most 1.")
    probabilities = softmax(logits)
    sorted_indices = np.argsort(
        probabilities
    )[::-1]
    sorted_probabilities = probabilities[
        sorted_indices
    ]
    cumulative_probabilities = np.cumsum(
        sorted_probabilities
    )
    # Keep the smallest group reaching the threshold.
    cutoff = np.searchsorted(
        cumulative_probabilities,
        p
    )
    keep_count = min(
        cutoff + 1,
        len(sorted_indices)
    )
    selected_indices = sorted_indices[:keep_count]
    selected_probabilities = probabilities[
        selected_indices
    ]
    selected_probabilities = (
        selected_probabilities
        / selected_probabilities.sum()
    )
    rng = np.random.default_rng(seed)
    selected_position = int(
        rng.choice(
            len(selected_indices),
            p=selected_probabilities
        )
    )
    return int(selected_indices[selected_position])
if __name__ == "__main__":
    logits = np.array([
        1.0,
        2.0,
        3.0,
        4.0,
        0.5
    ])
    result = top_p_sampling(
        logits,
        p=0.9,
        seed=42
    )
    print("Selected token:", result)