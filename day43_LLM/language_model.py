import numpy as np
class LanguageModel:
    def __init__(self, vocabulary_size):
        self.vocabulary_size = vocabulary_size
        self.transition_counts = np.zeros(
            (vocabulary_size, vocabulary_size),
            dtype=np.float64
        )
        self.probabilities = None
    def train(self, encoded_sentences):
        for sentence in encoded_sentences:
            for index in range(len(sentence) - 1):
                current_token = sentence[index]
                next_token = sentence[index + 1]
                self.transition_counts[
                    current_token,
                    next_token
                ] += 1
        # Add-one smoothing prevents zero probabilities.
        smoothed_counts = self.transition_counts + 1
        self.probabilities = (
            smoothed_counts
            / smoothed_counts.sum(axis=1, keepdims=True)
        )
    def predict_probabilities(self, current_token):
        if self.probabilities is None:
            raise RuntimeError("Train the model first.")
        return self.probabilities[current_token]
    def get_logits(self, current_token):
        probabilities = self.predict_probabilities(
            current_token
        )
        return np.log(probabilities)
if __name__ == "__main__":
    model = LanguageModel(vocabulary_size=5)
    training_data = [
        [1, 2, 3, 4],
        [1, 2, 4],
        [2, 3, 4]
    ]
    model.train(training_data)
    print("Next-token probabilities:")
    print(model.predict_probabilities(1))