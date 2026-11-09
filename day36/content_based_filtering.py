from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine
from movie_dataset import load_movies
def create_content_similarity(movies):
    movies = movies.copy()
    tfidf = TfidfVectorizer(
        stop_words="english"
    )
    tfidf_matrix = tfidf.fit_transform(
        movies["genres"].fillna("")
    )
    similarity = sklearn_cosine(tfidf_matrix)
    return movies, similarity
def recommend_similar_movies(movie_title, movies, similarity, top_n=10):
    matches = movies[
        movies["title"].str.contains(
            movie_title,
            case=False,
            regex=False,
            na=False
        )
    ]
    if matches.empty:
        print("Movie not found!")
        return
    index = matches.index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )
    results = []
    for movie_index, score in scores[1:top_n + 1]:
        results.append({
            "title": movies.iloc[movie_index]["title"],
            "similarity": score
        })
    return results
if __name__ == "__main__":
    movies = load_movies()
    movies, similarity = create_content_similarity(movies)
    recommendations = recommend_similar_movies(
        "Toy Story", movies, similarity
    )
    print("Similar Movies:")
    if recommendations:
        for movie in recommendations:
            print(movie)