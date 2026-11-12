
from tensorflow.keras.datasets import cifar10
def load_image_dataset():
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    print("CIFAR-10 dataset loaded successfully!")
    print("Training images:", X_train.shape)
    print("Testing images:", X_test.shape)
    class_names = [
        "Airplane",
        "Automobile",
        "Bird",
        "Cat",
        "Deer",
        "Dog",
        "Frog",
        "Horse",
        "Ship",
        "Truck"
    ]
    return X_train, y_train, X_test, y_test, class_names
if __name__ == "__main__":
    load_image_dataset()
