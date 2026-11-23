class Vocabulary:
    def __init__(self):
        self.word_to_id = {"<UNK>": 0}
        self.id_to_word = {0: "<UNK>"}
    def build(self, sentences):
        unique_words = sorted({
            word
            for sentence in sentences
            for word in sentence.split()
        })
        for word in unique_words:
            if word not in self.word_to_id:
                token_id = len(self.word_to_id)
                self.word_to_id[word] = token_id
                self.id_to_word[token_id] = word
    def encode(self, tokens):
        return [
            self.word_to_id.get(token, 0)
            for token in tokens
        ]
    def decode(self, token_ids):
        return [
            self.id_to_word.get(token_id, "<UNK>")
            for token_id in token_ids
        ]
    @property
    def size(self):
        return len(self.word_to_id)
if __name__ == "__main__":
    sentences = [
        "python is easy",
        "machine learning is useful"
    ]
    vocabulary = Vocabulary()
    vocabulary.build(sentences)
    print("Vocabulary:", vocabulary.word_to_id)
    print("Vocabulary size:", vocabulary.size)
    tokens = ["python", "is", "easy"]
    encoded = vocabulary.encode(tokens)
    print("Encoded:", encoded)
    print("Decoded:", vocabulary.decode(encoded))