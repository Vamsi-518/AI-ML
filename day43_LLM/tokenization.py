def tokenize(text):
    return text.split()

def encode_tokens(tokens, vocabulary):
    return [
        vocabulary.get(token, vocabulary["<UNK>"])
        for token in tokens
    ]
def decode_tokens(token_ids, reverse_vocabulary):
    return [
        reverse_vocabulary.get(token_id, "<UNK>")
        for token_id in token_ids
    ]
if __name__ == "__main__":
    sentence = "python is a programming language"
    tokens = tokenize(sentence)
    vocabulary = {
        "<UNK>": 0,
        "python": 1,
        "is": 2,
        "a": 3,
        "programming": 4,
        "language": 5
    }
    reverse_vocabulary = {
        value: key
        for key, value in vocabulary.items()
    }
    encoded = encode_tokens(tokens, vocabulary)
    decoded = decode_tokens(
        encoded,
        reverse_vocabulary
    )
    print("Tokens:", tokens)
    print("Encoded:", encoded)
    print("Decoded:", decoded)