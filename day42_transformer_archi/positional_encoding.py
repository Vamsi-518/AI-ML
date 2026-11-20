import numpy as np
def positional_encoding(sequence_length, embedding_dimension):
    positions = np.arange(sequence_length)[:, np.newaxis]
    dimensions = np.arange(embedding_dimension)[np.newaxis, :]
    angles = positions / np.power(
        10000,
        (2 * (dimensions // 2)) / embedding_dimension
    )
    encoding = np.zeros(
        (sequence_length, embedding_dimension)
    )
    encoding[:, 0::2] = np.sin(angles[:, 0::2])
    encoding[:, 1::2] = np.cos(angles[:, 1::2])
    return encoding
if __name__ == "__main__":
    result = positional_encoding(5, 8)
    print("Positional encoding shape:", result.shape)
    print(result)