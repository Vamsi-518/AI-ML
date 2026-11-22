import numpy as np
words = ["hello", "world", "AI", "transformer"]
embedding_size = 4
embeddings = np.random.rand(len(words), embedding_size)
for word, vector in zip(words, embeddings):
    print(word, ":", vector)