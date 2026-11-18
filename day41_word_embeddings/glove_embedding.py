import numpy as np
from sample_dataset import create_dataset
def build_cooccurrence(sentences, window_size=2):
    vocabulary = sorted({
        word
        for sentence in sentences
        for word in sentence
    })

    word_to_id = {
        word: index
        for index, word in enumerate(vocabulary)
    }

    matrix = np.zeros(
        (len(vocabulary), len(vocabulary)),
        dtype=np.float64
    )

    for sentence in sentences:
        for i, word in enumerate(sentence):
            start = max(0, i - window_size)
            end = min(len(sentence), i + window_size + 1)

            for j in range(start, end):
                if i != j:
                    distance = abs(i - j)
                    matrix[word_to_id[word]][word_to_id[sentence[j]]] += (
                        1.0 / distance
                    )
    return vocabulary, word_to_id, matrix
def train_glove(epochs=100, learning_rate=0.05):
    df = create_dataset()
    sentences = [
        sentence.lower().split()
        for sentence in df["sentence"]
    ]
    vocabulary, word_to_id, matrix = build_cooccurrence(sentences)
    vocab_size = len(vocabulary)
    dimensions = 30
    rng = np.random.default_rng(42)
    W = rng.normal(0, 0.1, (vocab_size, dimensions))
    C = rng.normal(0, 0.1, (vocab_size, dimensions))
    bias_w = np.zeros(vocab_size)
    bias_c = np.zeros(vocab_size)
    grad_sq_W = np.zeros_like(W)
    grad_sq_C = np.zeros_like(C)
    grad_sq_bw = np.zeros_like(bias_w)
    grad_sq_bc = np.zeros_like(bias_c)
    x_max = 100
    alpha = 0.75
    epsilon = 1e-8
    rows, cols = np.nonzero(matrix)
    for epoch in range(epochs):
        total_loss = 0.0
        for i, j in zip(rows, cols):
            x = matrix[i, j]
            weight = min((x / x_max) ** alpha, 1.0)
            target = np.log(x)
            prediction = (
                np.dot(W[i], C[j])
                + bias_w[i]
                + bias_c[j]
            )
            error = prediction - target
            total_loss += weight * error ** 2
            gradient = 2 * weight * error
            grad_w = gradient * C[j]
            grad_c = gradient * W[i]
            grad_sq_W[i] += grad_w ** 2
            grad_sq_C[j] += grad_c ** 2
            grad_sq_bw[i] += gradient ** 2
            grad_sq_bc[j] += gradient ** 2
            W[i] -= (
                learning_rate * grad_w
                / np.sqrt(grad_sq_W[i] + epsilon)
            )
            C[j] -= (
                learning_rate * grad_c
                / np.sqrt(grad_sq_C[j] + epsilon)
            )
            bias_w[i] -= (
                learning_rate * gradient
                / np.sqrt(grad_sq_bw[i] + epsilon)
            )
            bias_c[j] -= (
                learning_rate * gradient
                / np.sqrt(grad_sq_bc[j] + epsilon)
            )
        if (epoch + 1) % 20 == 0:
            print(
                f"Epoch {epoch + 1}, Loss: {total_loss:.4f}"
            )
    embeddings = W + C
    print("\nGloVe-style embeddings trained!")
    print("\nVector for king:")
    print(embeddings[word_to_id["king"]])
    return vocabulary, word_to_id, embeddings
if __name__ == "__main__":
    train_glove()
