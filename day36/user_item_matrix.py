from movie_dataset import load_ratings
from data_preprocessing import preprocess_ratings

def create_user_item_matrix(ratings):
    matrix = ratings.pivot_table(
        index="userId",
        columns="movieId",
        values="rating"
    )

    return matrix
if __name__ == "__main__":
    ratings = preprocess_ratings(load_ratings())
    user_item_matrix = create_user_item_matrix(ratings)
    print("User-Item Matrix:")
    print(user_item_matrix.head())
    print("\nMatrix Shape:", user_item_matrix.shape)