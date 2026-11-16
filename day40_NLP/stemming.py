
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
def perform_stemming(text):
    stemmer = PorterStemmer()
    words = word_tokenize(text)
    stemmed_words = [
        stemmer.stem(word)
        for word in words
    ]
    return stemmed_words
if __name__ == "__main__":
    text = "playing played plays studies studying"
    result = perform_stemming(text)
    print("Original:", text)
    print("Stemmed:", result)
