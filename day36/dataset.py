import pandas as pd
def load_movies():
    movies = pd.read_csv("movies.csv")
    return movies
def load_ratings():
    ratings = pd.read_csv("ratings.csv")
    return ratings
if __name__ == "__main__":
    movies = load_movies()
    ratings = load_ratings()
    print("Movies Dataset:")
    print(movies.head())
    print("\nRatings Dataset:")
    print(ratings.head())
    print("\nMovies Shape:", movies.shape)
    print("Ratings Shape:", ratings.shape)