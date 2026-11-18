
from gensim.models import Word2Vec
from sample_dataset import create_dataset
def train_word2vec():
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
    model.save("word2vec.model")
    print("Word2Vec model trained successfully!")
    print("\nVector for king:")
    print(model.wv["king"])
    print("\nSimilar words to king:")
    print(model.wv.most_similar("king", topn=5))
    return model
if __name__ == "__main__":
    train_word2vec()
