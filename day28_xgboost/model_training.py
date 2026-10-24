
from train_test_split import split_dataset
from xgboost_model import create_model
def train_model():
    X_train, X_test, y_train, y_test = split_dataset()
    model = create_model()
    model.fit(X_train, y_train)
    print("\nModel trained successfully!")
    return model, X_train, X_test, y_train, y_test
if __name__ == "__main__":
    train_model()
