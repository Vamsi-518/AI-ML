from sklearn.feature_extraction.text import (
    CountVectorizer,
    TfidfVectorizer
)
def compare_vectorization(sentences):
    # Bag of Words
    bow = CountVectorizer()
    bow_matrix = bow.fit_transform(sentences)
    print("Bag of Words Features:")
    print(bow.get_feature_names_out())
    print("\nBag of Words Matrix:")
    print(bow_matrix.toarray())
    # TF-IDF
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(sentences)
    print("\nTF-IDF Features:")
    print(tfidf.get_feature_names_out())
    print("\nTF-IDF Matrix:")
    print(tfidf_matrix.toarray())
if __name__ == "__main__":
    sentences = [
        "I love artificial intelligence",
        "Artificial intelligence is amazing",
        "I love machine learning"
    ]
    compare_vectorization(sentences)
