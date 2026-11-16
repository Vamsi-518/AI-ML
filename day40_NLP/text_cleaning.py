
import re
def clean_text(text):
    text = text.lower()
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)
    # Remove numbers
    text = re.sub(r"\d+", "", text)
    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text
if __name__ == "__main__":
    sample = "I LOVE this Product!!! Price: 500."
    result = clean_text(sample)
    print("Original Text:", sample)
    print("Cleaned Text:", result)
