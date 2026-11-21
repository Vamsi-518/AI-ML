import numpy as np
from scaled_dot_product_attention import (
    scaled_dot_product_attention
)
class SelfAttention:
    def __init__(self, embedding_dimension):
        rng = np.random.default_rng(42)
        self.query_weights = rng.normal(
            0, 0.1,
            (embedding_dimension, embedding_dimension)
        )
        self.key_weights = rng.normal(
            0, 0.1,
            (embedding_dimension, embedding_dimension)
        )
        self.value_weights = rng.normal(
            0, 0.1,
            (embedding_dimension, embedding_dimension)
        )
    def forward(self, inputs, mask=None):
        query = inputs @ self.query_weights
        key = inputs @ self.key_weights
        value = inputs @ self.value_weights
        output, weights = scaled_dot_product_attention(
            query,
            key,
            value,
            mask
        )
        return output, weights
if __name__ == "__main__":
    rng = np.random.default_rng(42)
    inputs = rng.random((4, 8))
    attention = SelfAttention(8)
    output, weights = attention.forward(inputs)
    print("Output shape:", output.shape)
    print("Attention weights:")
    print(weights)