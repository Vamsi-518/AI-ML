import numpy as np

from greedy_decoding import greedy_decoding
from temperature_sampling import temperature_sampling
from top_k_sampling import top_k_sampling
from top_p_sampling import top_p_sampling
def compare_sampling_methods(logits):
    print("SAMPLING TECHNIQUES COMPARISON")
    print("-" * 40)
    # Greedy decoding
    greedy_token = greedy_decoding(
        logits
    )
    print("Greedy:", greedy_token)
    # Temperature sampling
    temperature_token, probabilities = (
        temperature_sampling(
            logits,
            temperature=0.8,
            seed=42
        )
    )
    print("Temperature:", temperature_token)
    # Top-K sampling
    top_k_token = top_k_sampling(
        logits,
        k=3,
        seed=42
    )
    print("Top-K:", top_k_token)
    # Top-P sampling
    top_p_token = top_p_sampling(
        logits,
        p=0.9,
        seed=42
    )
    print("Top-P:", top_p_token)
    print("\nProbability distribution:")
    print(probabilities)
if __name__ == "__main__":
    logits = np.array([
        1.0,
        2.0,
        3.0,
        4.0,
        0.5
    ])
    compare_sampling_methods(logits)