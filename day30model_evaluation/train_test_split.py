
from sklearn.model_selection import train_test_split as split_data
from features_target import get_features_target
def split_dataset():
    X, y = get_features_target()
    X_train, X_test, y_train, y_test = split_data(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    print("\nTraining samples:", len(X_train))
    print("Testing samples:", len(X_test))
    return X_train, X_test, y_train, y_test
if __name__ == "__main__":
    split_dataset()
