from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
# Download tokenizer data
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
def tokenize_words(text):
    return word_tokenize(text)
def tokenize_sentences(text):
    return sent_tokenize(text)
if __name__ == "__main__":
    text = "I love Python. NLP is interesting."
    print("Words:")
    print(tokenize_words(text))
    print("\nSentences:")
    print(tokenize_sentences(text))
