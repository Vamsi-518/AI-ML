class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {
            "<PAD>": 0,
            "<UNK>": 1
        }
        self.id_to_word = {
            0: "<PAD>",
            1: "<UNK>"
        }
    def fit(self, sentences):
        words = sorted({
            word
            for sentence in sentences
            for word in sentence.split()
        })
        for word in words:
            if word not in self.word_to_id:
                token_id = len(self.word_to_id)
                self.word_to_id[word] = token_id
                self.id_to_word[token_id] = word
    def encode(self, sentence):
        return [
            self.word_to_id.get(word, 1)
            for word in sentence.split()
        ]
    def decode(self, token_ids):
        return " ".join(
            self.id_to_word.get(token_id, "<UNK>")
            for token_id in token_ids
        )
    @property
    def vocabulary_size(self):
        return len(self.word_to_id)
if __name__ == "__main__":
    tokenizer = SimpleTokenizer()
    sentences = [
        "python is interesting",
        "learning artificial intelligence"
    ]
    tokenizer.fit(sentences)
    encoded = tokenizer.encode(sentences[0])
    print("Vocabulary:", tokenizer.word_to_id)
    print("Encoded:", encoded)
    print("Decoded:", tokenizer.decode(encoded))