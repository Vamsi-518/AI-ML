import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
def calculate_similarity(vector1, vector2):
    vector1 = np.array(vector1).reshape(1, -1)
    vector2 = np.array(vector2).reshape(1, -1)
    score = cosine_similarity(vector1, vector2)[0][0]
    return score
if __name__ == "__main__":
    king = [0.8, 0.7, 0.2, 0.9]
    queen = [0.7, 0.8, 0.3, 0.9]
    dog = [0.1, 0.2, 0.9, 0.1]
    print(
        "King and Queen:",
        calculate_similarity(king, queen)
    )
    print(
        "King and Dog:",
        calculate_similarity(king, dog)
    )
