
from gensim.models import Word2Vec
from sample_dataset import create_dataset
def train_skipgram():
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
    model.save("skipgram.model")
    print("Skip-Gram model trained successfully!")
    print("\nVector for python:")
    print(model.wv["python"])
    print("\nSimilar words to python:")
    print(model.wv.most_similar("python", topn=5))
    return model
if __name__ == "__main__":
    train_skipgram()
