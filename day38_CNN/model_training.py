
from image_dataset import load_image_dataset
from data_preprocessing import preprocess_images
from cnn_model import build_cnn_model
def train_cnn_model(epochs=10):
    X_train, y_train, X_test, y_test, class_names = (
        load_image_dataset()
    )
    X_train, X_test, y_train, y_test = preprocess_images(
        X_train,
        X_test,
        y_train,
        y_test
    )
    model = build_cnn_model()
    history = model.fit(
        X_train,
        y_train,
        epochs=epochs,
        batch_size=64,
        validation_split=0.2,
        verbose=1
    )
    print("CNN model training completed!")
    return model, history, X_test, y_test, class_names
if __name__ == "__main__":
    train_cnn_model()
