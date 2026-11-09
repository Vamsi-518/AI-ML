from movie_dataset import load_movies, load_ratings
def popular_movies(movies, ratings, top_n=10):
    movie_stats = ratings.groupby("movieId").agg(
        average_rating=("rating", "mean"),
        rating_count=("rating", "count")
    ).reset_index()
    minimum_votes = 20
    popular = movie_stats[
        movie_stats["rating_count"] >= minimum_votes
    ]
    popular = popular.merge(
        movies,
        on="movieId"
    )
    popular = popular.sort_values(
        by=["average_rating", "rating_count"],
        ascending=False
    )
    return popular[
        ["title", "genres", "average_rating", "rating_count"]
    ].head(top_n)
if __name__ == "__main__":
    movies = load_movies()
    ratings = load_ratings()
    recommendations = popular_movies(
        movies, ratings
    )
    print("Top Popular Movies:")
    print(recommendations.to_string(index=False))