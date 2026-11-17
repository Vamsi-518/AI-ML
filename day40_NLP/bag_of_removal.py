from sklearn.feature_extraction.text import CountVectorizer
def create_bag_of_words(sentences):
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(sentences)
    print("Vocabulary:")
    print(vectorizer.get_feature_names_out())
    print("\nWord Count Matrix:")
    print(matrix.toarray())
    return matrix
if __name__ == "__main__":
    sentences = [
        "I love Python",
        "Python is amazing",
        "I love machine learning"
    ]
    create_bag_of_words(sentences)
