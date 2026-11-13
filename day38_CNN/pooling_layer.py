
import matplotlib.pyplot as plt
from tensorflow.keras.layers import MaxPooling2D
def demonstrate_pooling(image):
    image = image.reshape(1, 32, 32, 3)
    pooling = MaxPooling2D(pool_size=(2, 2))
    output = pooling(image)
    pooled_image = output.numpy()[0]
    plt.figure(figsize=(5, 5))
    plt.imshow(pooled_image.astype("float32"))
    plt.title("Max Pooling Output")
    plt.axis("off")
    plt.show()
    print("Original shape:", image.shape)
    print("Pooled shape:", output.shape)
    return pooled_image
if __name__ == "__main__":
    from image_dataset import load_image_dataset
    X_train, y_train, X_test, y_test, names = load_image_dataset()
    demonstrate_pooling(X_train[0])
