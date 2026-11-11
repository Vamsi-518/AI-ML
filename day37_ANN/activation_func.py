
import numpy as np
def relu(x):
    return np.maximum(0, x)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def tanh(x):
    return np.tanh(x)
def softmax(x):
    shifted = x - np.max(x)
    exp_values = np.exp(shifted)
    return exp_values / np.sum(exp_values)
if __name__ == "__main__":
    values = np.array([-2, -1, 0, 1, 2])
    print("Input:", values)
    print("ReLU:", relu(values))
    print("Sigmoid:", sigmoid(values))
    print("Tanh:", tanh(values))
    print("Softmax:", softmax(values))
