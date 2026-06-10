from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
import requests

app = Flask(__name__)
API_KEY = "20ca9cf0affa448d92a70e1d79fa1fab"

def get_cover_data(game_name):

    url = (
        f"https://api.rawg.io/api/games"
        f"?key={API_KEY}"
        f"&search={game_name}"  
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None
    
    data = response.json()

    results = data.get("results")

    if not results:
        return None

    game = results[0]
    genres = ", ".join(
        g["name"]
        for g in game.get("genres", [])
    )

    return {
        "cover_url": game.get("background_image"),
        "genres": genres or "Desconhecido",
        "release_date": game.get("released"),
        "rating": game.get("rating"),
    }
 

@app.route("/")
def home():
    

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()

    conn.close()

    return render_template("index.html", games=games)


@app.route("/add", methods=["POST"])
def add_game():

    nome = request.form["nome"]
    status = request.form["status"]
    game_data = get_cover_data(nome)
    
    print(game_data)

    if game_data:
        genre = game_data["genres"]
        cover_url = game_data["cover_url"]
        release_date = game_data["release_date"]
        rating = game_data["rating"]

    else:
        genre = "Desconhecido"
        cover_url = None
        release_date = None
        rating = None
    

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO games (name, genre, status, cover_url, release_date, rating) VALUES (?, ?, ?, ?, ?, ?)",
                   (nome, genre, status, cover_url, release_date, rating))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/random")
def random_game():

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM games")

    games = cursor.fetchall()
    conn.close()

    if not games:
        return render_template(
            "random_game.html", game=None
        )

    zero_weight = 0.5
    weights = []
    for g in games:
        status = (g[3] or "").strip().lower()
        weights.append(zero_weight if status == "zerado" else 1.0)

    selected_game = random.choices(games, weights=weights, k=1)[0]
    return render_template(
        "random_game.html", game=selected_game
    )


@app.route("/delete/<int:game_id>", methods=["POST"])
def delete_game(game_id):

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM games WHERE id = ?", (game_id,))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/update_status/<int:game_id>", methods=["POST"])
def update_status(game_id):
    new_status = request.form.get("status")

    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE games SET status = ? WHERE id = ?", (new_status, game_id))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)


