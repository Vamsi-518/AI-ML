
def preprocess_images(X_train, X_test, y_train, y_test):
    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0
    y_train = y_train.flatten()
    y_test = y_test.flatten()
    print("Image preprocessing completed!")
    return X_train, X_test, y_train, y_test
if __name__ == "__main__":
    from image_dataset import load_image_dataset
    X_train, y_train, X_test, y_test, names = load_image_dataset()
    X_train, X_test, y_train, y_test = preprocess_images(
        X_train, X_test, y_train, y_test
    )
    print("Processed training shape:", X_train.shape)
