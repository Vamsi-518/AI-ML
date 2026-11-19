
from gensim.models import Word2Vec
from sample_dataset import create_dataset
def train_model():
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
    return model
def find_similar_words(model, input_word):
    if input_word not in model.wv:
        print(f"'{input_word}' is not in the vocabulary.")
        return
    similar_words = model.wv.most_similar(
        input_word,
        topn=5
    )
    print(f"\nWords similar to '{input_word}':")
    for word, score in similar_words:
        print(f"{word}: {score:.4f}")
if __name__ == "__main__":
    model = train_model()
    find_similar_words(model, "king")
    find_similar_words(model, "python")
