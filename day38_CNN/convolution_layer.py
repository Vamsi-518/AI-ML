
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D
def demonstrate_convolution(image):
    image = np.expand_dims(image, axis=0)
    layer = Conv2D(
        filters=1,
        kernel_size=(3, 3),
        activation="relu",
        padding="valid"
    )
    output = layer(image)
    feature_map = output.numpy()[0, :, :, 0]
    plt.figure(figsize=(5, 5))
    plt.imshow(feature_map, cmap="gray")
    plt.title("Convolution Feature Map")
    plt.axis("off")
    plt.show()
    return feature_map
if __name__ == "__main__":
    from image_dataset import load_image_dataset
    from data_preprocessing import preprocess_images
    X_train, y_train, X_test, y_test, names = load_image_dataset()
    X_train, X_test, y_train, y_test = preprocess_images(
        X_train, X_test, y_train, y_test
    )
    demonstrate_convolution(X_train[0])
