from sklearn.preprocessing import OneHotEncoder
import numpy as np
def perform_one_hot_encoding(words):
    unique_words = sorted(set(words))
    encoder = OneHotEncoder(
        sparse_output=False,
        handle_unknown="ignore"
    )
    encoded = encoder.fit_transform(
        np.array(unique_words).reshape(-1, 1)
    )
    for word, vector in zip(unique_words, encoded):
        print(f"{word}: {vector}")
if __name__ == "__main__":
    words = ["cat", "dog", "king", "queen", "dog"]
    perform_one_hot_encoding(words)
