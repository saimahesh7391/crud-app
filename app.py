from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake DB
movies = []
id_counter = 1


# ✅ CREATE Movie
@app.route('/movies', methods=['POST'])
def create_movie():
    global id_counter

    data = request.json

    # Basic validation
    if not data.get("title"):
        return {"error": "Title is required"}, 400

    movie = {
        "id": id_counter,
        "title": data.get("title"),
        "director": data.get("director"),
        "year": data.get("year"),
        "rating": data.get("rating")
    }

    movies.append(movie)
    id_counter += 1

    return jsonify(movie), 201


# ✅ READ ALL Movies
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)


# ✅ READ ONE Movie
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie)

    return {"error": "Movie not found"}, 404


# ✅ UPDATE Movie
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.json

    for movie in movies:
        if movie["id"] == movie_id:
            movie["title"] = data.get("title", movie["title"])
            movie["director"] = data.get("director", movie["director"])
            movie["year"] = data.get("year", movie["year"])
            movie["rating"] = data.get("rating", movie["rating"])

            return jsonify(movie)

    return {"error": "Movie not found"}, 404


# ✅ DELETE Movie
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies

    movies = [m for m in movies if m["id"] == movie_id]

    return {"message": "Movie deleted"}


if __name__ == '__main__':
    app.run(debug=True)