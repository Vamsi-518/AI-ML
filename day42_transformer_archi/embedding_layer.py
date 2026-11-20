import numpy as np
class EmbeddingLayer:
    def __init__(self, vocabulary_size, embedding_dimension):
        rng = np.random.default_rng(42)
        self.embeddings = rng.normal(
            0,
            0.02,
            (vocabulary_size, embedding_dimension)
        )
    def forward(self, token_ids):
        return self.embeddings[np.array(token_ids)]
if __name__ == "__main__":
    layer = EmbeddingLayer(20, 8)
    output = layer.forward([2, 4, 6])
    print("Embedding shape:", output.shape)
    print(output)