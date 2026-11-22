import numpy as np
def positional_encoding(sequence_length, embedding_size):
    encoding = np.zeros((sequence_length, embedding_size))
    for pos in range(sequence_length):
        for i in range(embedding_size):
            angle = pos / (10000 ** (2 * (i // 2) / embedding_size))
            if i % 2 == 0:
                encoding[pos, i] = np.sin(angle)
            else:
                encoding[pos, i] = np.cos(angle)
    return encoding
result = positional_encoding(4, 6)
print("Positional Encoding:")
print(result)