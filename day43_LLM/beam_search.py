import numpy as np
def beam_search(
    model,
    start_token,
    beam_width=3,
    max_length=5
):
    beams = [([start_token], 0.0)]
    for _ in range(max_length):
        candidates = []
        for sequence, score in beams:
            current_token = sequence[-1]
            probabilities = model.predict_probabilities(
                current_token
            )
            top_tokens = np.argsort(
                probabilities
            )[-beam_width:]
            for token in top_tokens:
                probability = probabilities[token]
                new_score = score + np.log(
                    max(probability, 1e-12)
                )
                new_sequence = sequence + [int(token)]
                candidates.append(
                    (new_sequence, new_score)
                )
        beams = sorted(
            candidates,
            key=lambda item: item[1],
            reverse=True
        )[:beam_width]
    return beams
if __name__ == "__main__":
    from language_model import LanguageModel
    model = LanguageModel(5)
    model.train([
        [1, 2, 3, 4],
        [1, 2, 4],
        [2, 3, 4]
    ])
    results = beam_search(
        model,
        start_token=1,
        beam_width=2,
        max_length=3
    )
    for sequence, score in results:
        print("Sequence:", sequence)
        print("Score:", score)