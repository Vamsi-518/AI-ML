import numpy as np
def softmax(values, axis=-1):
    values = values - np.max(
        values,
        axis=axis,
        keepdims=True
    )
    exp_values = np.exp(values)
    return exp_values / np.sum(
        exp_values,
        axis=axis,
        keepdims=True
    )
def scaled_dot_product_attention(
    query,
    key,
    value,
    mask=None
):
    dimension = query.shape[-1]
    scores = np.matmul(
        query,
        np.swapaxes(key, -2, -1)
    ) / np.sqrt(dimension)
    if mask is not None:
        scores = np.where(mask, scores, -1e9)
    attention_weights = softmax(scores)
    output = np.matmul(
        attention_weights,
        value
    )
    return output, attention_weights
if __name__ == "__main__":
    rng = np.random.default_rng(42)
    query = rng.random((3, 4))
    key = rng.random((3, 4))
    value = rng.random((3, 4))
    output, weights = scaled_dot_product_attention(
        query, key, value
    )
    print("Attention output:")
    print(output)
    print("Attention weights:")
    print(weights)