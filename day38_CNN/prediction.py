
import numpy as np
def predict_image(model, image, class_names):
    image = np.expand_dims(image, axis=0)
    probabilities = model.predict(image, verbose=0)
    predicted_index = np.argmax(probabilities[0])
    predicted_class = class_names[predicted_index]
    confidence = probabilities[0][predicted_index] * 100
    print("Predicted class:", predicted_class)
    print(f"Confidence: {confidence:.2f}%")
    return predicted_class
if __name__ == "__main__":
    from model_training import train_cnn_model
    model, history, X_test, y_test, class_names = train_cnn_model()
    predict_image(model, X_test[0], class_names)
