import numpy as np
def predict_next_token(model, current_token, reverse_vocabulary):
    probabilities = model.predict_probabilities(
        current_token
    )
    predicted_id = int(np.argmax(probabilities))
    predicted_word = reverse_vocabulary.get(
        predicted_id,
        "<UNK>"
    )
    return predicted_word, probabilities
if __name__ == "__main__":
    from language_model import LanguageModel
    model = LanguageModel(5)
    model.train([
        [1, 2, 3, 4],
        [1, 2, 4],
        [2, 3, 4]
    ])
    reverse_vocabulary = {
        0: "<UNK>",
        1: "python",
        2: "is",
        3: "easy",
        4: "useful"
    }
    word, probabilities = predict_next_token(
        model,
        1,
        reverse_vocabulary
    )
    print("Predicted next word:", word)
    print("Probabilities:", probabilities)