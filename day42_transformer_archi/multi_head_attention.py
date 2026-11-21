import numpy as np

from scaled_dot_product_attention import (
    scaled_dot_product_attention
)
class MultiHeadAttention:
    def __init__(self, embedding_dimension, number_of_heads):
        if embedding_dimension % number_of_heads != 0:
            raise ValueError(
                "Embedding dimension must be divisible by heads"
            )
        self.embedding_dimension = embedding_dimension
        self.number_of_heads = number_of_heads
        self.head_dimension = (
            embedding_dimension // number_of_heads
        )
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
        self.output_weights = rng.normal(
            0, 0.1,
            (embedding_dimension, embedding_dimension)
        )
    def split_heads(self, values):
        sequence_length = values.shape[0]
        values = values.reshape(
            sequence_length,
            self.number_of_heads,
            self.head_dimension
        )
        return values.transpose(1, 0, 2)
    def forward(self, inputs, mask=None):
        query = self.split_heads(
            inputs @ self.query_weights
        )
        key = self.split_heads(
            inputs @ self.key_weights
        )
        value = self.split_heads(
            inputs @ self.value_weights
        )
        attention_outputs = []
        for head in range(self.number_of_heads):
            output, _ = scaled_dot_product_attention(
                query[head],
                key[head],
                value[head],
                mask
            )
            attention_outputs.append(output)
        combined = np.concatenate(
            attention_outputs,
            axis=-1
        )
        return combined @ self.output_weights
if __name__ == "__main__":
    rng = np.random.default_rng(42)
    inputs = rng.random((5, 8))
    attention = MultiHeadAttention(
        embedding_dimension=8,
        number_of_heads=2
    )
    output = attention.forward(inputs)
    print("Multi-head output shape:", output.shape)
    print(output)