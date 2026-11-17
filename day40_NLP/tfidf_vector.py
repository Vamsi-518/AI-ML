
from sklearn.feature_extraction.text import TfidfVectorizer
def create_tfidf(sentences):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(sentences)
    print("Vocabulary:")
    print(vectorizer.get_feature_names_out())
    print("\nTF-IDF Matrix:")
    print(matrix.toarray())
    return matrix
if __name__ == "__main__":
    sentences = [
        "Python is easy to learn",
        "Machine learning is interesting",
        "Python is useful for machine learning"
    ]
    create_tfidf(sentences)
