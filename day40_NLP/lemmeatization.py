
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)
def perform_lemmatization(text):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    tagged_words = nltk.pos_tag(words)
    def get_wordnet_pos(tag):
        if tag.startswith("J"):
            return wordnet.ADJ
        elif tag.startswith("V"):
            return wordnet.VERB
        elif tag.startswith("N"):
            return wordnet.NOUN
        elif tag.startswith("R"):
            return wordnet.ADV
        return wordnet.NOUN
    result = []
    for word, tag in tagged_words:
        pos = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word, pos)
        result.append(lemma)
    return result
if __name__ == "__main__":
    text = "The students are studying and playing games"
    print("Original:", text)
    print("Lemmatized:", perform_lemmatization(text))
