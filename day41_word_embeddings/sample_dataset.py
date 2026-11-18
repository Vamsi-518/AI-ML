
import pandas as pd
def create_dataset():
    sentences = [
        "king is a powerful man",
        "queen is a powerful woman",
        "king and queen rule the kingdom",
        "prince is the son of a king",
        "princess is the daughter of a queen",
        "man and woman are human beings",
        "dog is a friendly animal",
        "cat is a lovely animal",
        "dog and cat are pets",
        "python is a programming language",
        "machine learning is a part of artificial intelligence",
        "deep learning uses neural networks",
        "artificial intelligence is changing technology",
        "python is useful for machine learning",
        "data science uses python programming",
        "computer science studies technology",
        "a king lives in a palace",
        "a queen lives in a palace",
        "the prince lives in a kingdom",
        "the princess lives in a kingdom"
    ]
    return pd.DataFrame({"sentence": sentences})
if __name__ == "__main__":
    df = create_dataset()
    print("Sample Dataset:")
    print(df)
    print("\nTotal sentences:", len(df))
