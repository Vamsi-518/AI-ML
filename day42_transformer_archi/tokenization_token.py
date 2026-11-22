text = "I am learning Transformer Architecture"
tokens = text.lower().split()
print("Original Text:", text)
print("Tokens:", tokens)
for i, token in enumerate(tokens):
    print(token, ":", i + 1)