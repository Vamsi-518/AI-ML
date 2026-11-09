import pandas as pd
from movie_dataset import load_movies, load_ratings
def preprocess_movies(movies):
    movies = movies.drop_duplicates(subset="movieId")
    movies["title"] = movies["title"].fillna("")
    movies["genres"] = movies["genres"].fillna("")
    return movies
def preprocess_ratings(ratings):
    ratings = ratings.dropna()
    ratings = ratings.drop_duplicates(
        subset=["userId", "movieId"]
    )
    return ratings
if __name__ == "__main__":
    movies = preprocess_movies(load_movies())
    ratings = preprocess_ratings(load_ratings())
    print("Preprocessed Movies:")
    print(movies.head())
    print("\nPreprocessed Ratings:")
    print(ratings.head())
    print("\nMissing Values:")
    print(ratings.isnull().sum())