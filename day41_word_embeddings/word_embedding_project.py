
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
from sample_dataset import create_dataset
def visualize_embeddings():
    df = create_dataset()
    sentences = [
        sentence.lower().split()
        for sentence in df["sentence"]
    ]
    model = Word2Vec(
        sentences=sentences,
        vector_size=50,
        window=3,
        min_count=1,
        workers=1,
        sg=1,
        epochs=200,
        seed=42
    )
    words = list(model.wv.index_to_key)
    vectors = [
        model.wv[word]
        for word in words
    ]
    pca = PCA(n_components=2)
    reduced_vectors = pca.fit_transform(vectors)
    plt.figure(figsize=(12, 8))
    plt.scatter(
        reduced_vectors[:, 0],
        reduced_vectors[:, 1]
    )
    for i, word in enumerate(words):
        plt.annotate(
            word,
            (reduced_vectors[i, 0], reduced_vectors[i, 1])
        )
    plt.title("Word Embedding Visualization using PCA")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    visualize_embeddings()
