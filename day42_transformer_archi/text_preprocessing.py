import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
def preprocess_sentences(sentences):
    return [clean_text(sentence) for sentence in sentences]
if __name__ == "__main__":
    examples = [
        "Hello, AI World!",
        "Python is AMAZING."
    ]
    for sentence in preprocess_sentences(examples):
        print(sentence)