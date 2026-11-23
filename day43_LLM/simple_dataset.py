sentences = [
    "artificial intelligence is changing the world",
    "machine learning is a part of artificial intelligence",
    "deep learning uses neural networks",
    "python is a popular programming language",
    "python is useful for machine learning",
    "data science uses statistics and programming",
    "natural language processing works with text",
    "language models predict the next word",
    "large language models generate text",
    "artificial intelligence helps solve problems",
    "neural networks learn patterns from data",
    "machine learning can make predictions",
    "python is easy to learn",
    "data is important for artificial intelligence",
    "deep learning is used in computer vision",
]
def get_dataset():
    return sentences
if __name__ == "__main__":
    for index, sentence in enumerate(get_dataset(), start=1):
        print(f"{index}. {sentence}")