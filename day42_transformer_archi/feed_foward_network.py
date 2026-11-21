import numpy as np
class FeedForwardNetwork:
    def __init__(
        self,
        embedding_dimension,
        hidden_dimension
    ):
        rng = np.random.default_rng(42)
        self.weights_1 = rng.normal(
            0, 0.1,
            (embedding_dimension, hidden_dimension)
        )
        self.bias_1 = np.zeros(hidden_dimension)
        self.weights_2 = rng.normal(
            0, 0.1,
            (hidden_dimension, embedding_dimension)
        )
        self.bias_2 = np.zeros(embedding_dimension)
    def forward(self, inputs):
        hidden = (
            inputs @ self.weights_1
            + self.bias_1
        )
        hidden = np.maximum(0, hidden)  # ReLU
        output = (
            hidden @ self.weights_2
            + self.bias_2
        )
        return output
if __name__ == "__main__":
    rng = np.random.default_rng(42)
    inputs = rng.random((5, 8))
    network = FeedForwardNetwork(8, 16)
    output = network.forward(inputs)
    print("Feed-forward output shape:", output.shape)