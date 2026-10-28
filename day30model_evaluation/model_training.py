
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from train_test_split import split_dataset
def train_model():
    X_train, X_test, y_train, y_test = split_dataset()
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])
    model.fit(X_train, y_train)
    print("\nModel trained successfully!")
    return model, X_train, X_test, y_train, y_test
if __name__ == "__main__":
    train_model()
