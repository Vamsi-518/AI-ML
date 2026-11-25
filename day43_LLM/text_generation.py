from sample_dataset import get_dataset
from text_preprocessing import preprocess_sentences
from vocabulary import Vocabulary
from language_model import LanguageModel
from greedy_decoding import greedy_decoding


def generate_text(
    model,
    vocabulary,
    starting_text,
    max_new_tokens=10
):

    words = starting_text.lower().split()

    generated_ids = vocabulary.encode(words)

    if not generated_ids:
        raise ValueError("Starting text cannot be empty.")

    for _ in range(max_new_tokens):

        current_token = generated_ids[-1]

        probabilities = model.predict_probabilities(
            current_token
        )

        next_token = greedy_decoding(probabilities)

        generated_ids.append(next_token)

    generated_words = vocabulary.decode(
        generated_ids
    )

    return " ".join(generated_words)


def main():

    sentences = get_dataset()

    cleaned_sentences = preprocess_sentences(
        sentences
    )

    vocabulary = Vocabulary()

    vocabulary.build(cleaned_sentences)

    encoded_sentences = []

    for sentence in cleaned_sentences:

        tokens = sentence.split()

        encoded = vocabulary.encode(tokens)

        encoded_sentences.append(encoded)

    model = LanguageModel(
        vocabulary.size
    )

    model.train(encoded_sentences)

    starting_text = "artificial intelligence"

    generated = generate_text(
        model,
        vocabulary,
        starting_text,
        max_new_tokens=10
    )

    print("Starting text:", starting_text)
    print("\nGenerated text:")
    print(generated)


if __name__ == "__main__":
    main()