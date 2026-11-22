
import numpy as np
def self_attention(query, key, value):
    scores = np.dot(query, key.T)
    scores = scores / np.sqrt(key.shape[-1])
    attention = np.exp(scores)
    attention = attention / np.sum(attention, axis=-1, keepdims=True)
    output = np.dot(attention, value)
    return output
query = np.array([[1, 0], [0, 1]])
key = np.array([[1, 0], [0, 1]])
value = np.array([[10, 20], [30, 40]])
result = self_attention(query, key, value)
print("Self Attention Output:")
print(result)