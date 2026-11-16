
import pandas as pd
def create_dataset():
    data = {
        "text": [
            "I love this product",
            "This product is amazing",
            "Excellent quality and great service",
            "I am very happy with this purchase",
            "The product is fantastic",
            "Wonderful experience",
            "I really like this product",
            "Very good quality",
            "The service was excellent",
            "Absolutely loved it",
            "I hate this product",
            "This product is terrible",
            "Very poor quality",
            "I am disappointed with this purchase",
            "The product is awful",
            "Bad customer experience",
            "I do not like this product",
            "Very bad service",
            "The quality is horrible",
            "I regret buying this"
        ],
        "sentiment": [
            "Positive", "Positive", "Positive", "Positive",
            "Positive", "Positive", "Positive", "Positive",
            "Positive", "Positive",
            "Negative", "Negative", "Negative", "Negative",
            "Negative", "Negative", "Negative", "Negative",
            "Negative", "Negative"
        ]
    }
    return pd.DataFrame(data)
if __name__ == "__main__":
    df = create_dataset()
    print(df.head())
    print("\nDataset information:")
    print(df.info())
    print("\nSentiment distribution:")
    print(df["sentiment"].value_counts())
