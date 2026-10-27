
from sklearn.datasets import load_iris
from model_training import train_model
def make_predictions():
    model, X_train, X_test, y_train, y_test = train_model()
    predictions = model.predict(X_test)
    iris = load_iris()
    print("\nActual values:")
    print(y_test.to_numpy())
    print("\nPredicted values:")
    print(predictions)
    print("\nPredicted species for first five samples:")
    for prediction in predictions[:5]:
        print(iris.target_names[int(prediction)])
    return y_test, predictions
if __name__ == "__main__":
    make_predictions()
