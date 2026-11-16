
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    filtered_words = [
        word for word in words
        if word.lower() not in stop_words
    ]
    return filtered_words
if __name__ == "__main__":
    text = "This is a very good product and I love it."
    result = remove_stopwords(text)
    print("Original:", text)
    print("After Stopword Removal:", result)
