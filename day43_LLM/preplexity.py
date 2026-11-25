import numpy as np
def calculate_perplexity(model, encoded_sentence):
    if len(encoded_sentence) < 2:
        raise ValueError(
            "Sentence must contain at least two tokens."
        )
    total_log_probability = 0.0
    count = 0
    for index in range(len(encoded_sentence) - 1):
        current_token = encoded_sentence[index]
        next_token = encoded_sentence[index + 1]
        probabilities = model.predict_probabilities(
            current_token
        )
        probability = probabilities[next_token]
        total_log_probability += np.log(
            max(probability, 1e-12)
        )
        count += 1
    average_log_probability = (
        total_log_probability / count
    )
    perplexity = np.exp(
        -average_log_probability
    )
    return perplexity
if __name__ == "__main__":
    from language_model import LanguageModel
    model = LanguageModel(5)
    training_data = [
        [1, 2, 3, 4],
        [1, 2, 4],
        [2, 3, 4]
    ]
    model.train(training_data)
    test_sentence = [1, 2, 3, 4]
    result = calculate_perplexity(
        model,
        test_sentence
    )
    print("Test sentence:", test_sentence)
    print("Perplexity:", result)