from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = [
    {"title": "The Matrix", "genres": "Action Sci-Fi"},
    {"title": "Inception", "genres": "Action Adventure Sci-Fi"},
    {"title": "The Notebook", "genres": "Romance Drama"},
    {"title": "Avengers", "genres": "Action Adventure"},
    {"title": "The Conjuring", "genres": "Horror Thriller"},
    {"title": "Interstellar", "genres": "Adventure Drama Sci-Fi"},
    {"title": "La La Land", "genres": "Romance Musical Drama"},
]

def find_genres_by_title(title):
    title = title.lower()
    for movie in movies:
        if movie["title"].lower() == title:
            return movie["genres"]
    return None

def recommend(user_input, movies, top_n=3):
    genres = find_genres_by_title(user_input)
    if genres:
        print(f"Using genres from movie '{user_input}': {genres}")
    else:
        genres = user_input
        print(f"No exact movie match found. Using input as genres: {genres}")

    corpus = [movie["genres"] for movie in movies] + [genres]
    vectorizer = CountVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()

    cosine_sim = cosine_similarity([vectors[-1]], vectors[:-1])[0]
    scored_movies = sorted(
        [(movies[i]["title"], score) for i, score in enumerate(cosine_sim)],
        key=lambda x: x[1],
        reverse=True
    )

    return scored_movies[:top_n]

def main():
    print("Welcome! Enter a movie title or genres to get recommendations.")
    user_input = input("Your input: ").strip()
    recommendations = recommend(user_input, movies)
    print("\nTop recommendations:")
    for title, score in recommendations:
        print(f"{title} (Match score: {score:.2f})")

if __name__ == "__main__":
    main()
