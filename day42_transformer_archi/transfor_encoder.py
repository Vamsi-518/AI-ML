import numpy as np

from multi_head_attention import MultiHeadAttention
from feed_forward_network import FeedForwardNetwork


def layer_normalization(inputs, epsilon=1e-6):

    mean = np.mean(inputs, axis=-1, keepdims=True)

    variance = np.var(inputs, axis=-1, keepdims=True)

    return (
        (inputs - mean)
        / np.sqrt(variance + epsilon)
    )


class TransformerEncoder:

    def __init__(
        self,
        embedding_dimension,
        number_of_heads,
        hidden_dimension
    ):

        self.attention = MultiHeadAttention(
            embedding_dimension,
            number_of_heads
        )

        self.feed_forward = FeedForwardNetwork(
            embedding_dimension,
            hidden_dimension
        )

    def forward(self, inputs, mask=None):

        attention_output = self.attention.forward(
            inputs,
            mask
        )

        attention_output = layer_normalization(
            inputs + attention_output
        )

        feed_forward_output = self.feed_forward.forward(
            attention_output
        )

        output = layer_normalization(
            attention_output + feed_forward_output
        )

        return output


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    inputs = rng.random((5, 8))

    encoder = TransformerEncoder(8, 2, 16)

    output = encoder.forward(inputs)

    print("Encoder output shape:", output.shape)
    print(output)