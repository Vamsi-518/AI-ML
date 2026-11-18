
from gensim.models import Word2Vec

from sample_dataset import create_dataset


def train_cbow():
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
        sg=0,
        epochs=200,
        seed=42
    )

    model.save("cbow.model")

    print("CBOW model trained successfully!")

    print("\nVector for queen:")
    print(model.wv["queen"])

    print("\nSimilar words to queen:")
    print(model.wv.most_similar("queen", topn=5))

    return model


if __name__ == "__main__":
    train_cbow()
