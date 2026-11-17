
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
from sample_dataset import create_dataset
from text_cleaning import clean_text
def run_nlp_project():
    # 1. Load dataset
    df = create_dataset()
    X = df["text"].apply(clean_text)
    y = df["sentiment"]
    print("Dataset:")
    print(df.head())
    # 2. Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y
    )
    # 3. TF-IDF vectorization
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2)
    )
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    # 4. Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vectorized, y_train)
    # 5. Predictions
    y_pred = model.predict(X_test_vectorized)
    # 6. Model evaluation
    accuracy = accuracy_score(y_test, y_pred)
    print("\nModel Accuracy:", accuracy)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    # 7. Confusion matrix
    cm = confusion_matrix(
        y_test,
        y_pred,
        labels=model.classes_
    )
    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=model.classes_
    )
    display.plot(cmap="Blues")
    plt.title("NLP Sentiment Analysis")
    plt.tight_layout()
    plt.show()
    # 8. Predict new reviews
    new_reviews = [
        "This product is excellent",
        "I hate this terrible product",
        "Amazing quality and wonderful service"
    ]
    cleaned_reviews = [
        clean_text(review)
        for review in new_reviews
    ]
    review_vectors = vectorizer.transform(cleaned_reviews)
    predictions = model.predict(review_vectors)
    print("\nNew Review Predictions:")
    for review, prediction in zip(new_reviews, predictions):
        print(f"Review: {review}")
        print(f"Sentiment: {prediction}")
        print("-" * 40)
if __name__ == "__main__":
    run_nlp_project()
