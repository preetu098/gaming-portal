from flask import Flask, render_template

app = Flask(__name__)


games_data = {
    "pubg": {
        "title": "PUBG",
        "description": "Battle Royale Survival Game",
        "icon": "🎯"
    },

    "freefire": {
        "title": "Free Fire",
        "description": "Fast Paced Action Game",
        "icon": "🔥"
    },

    "minecraft": {
        "title": "Minecraft",
        "description": "Build Your Own World",
        "icon": "⛏️"
    }
}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/games')
def games():
    return render_template(
        'games.html',
        games=games_data
    )


@app.route('/game/<game_name>')
def game(game_name):

    game = games_data.get(game_name)

    if game:
        return render_template(
            'game.html',
            game=game
        )

    return "<h1>Game Not Found</h1>"


@app.route('/leaderboard')
def leaderboard():

    players = [

        {"name": "Pratibha", "score": 980},

        {"name": "Radhika", "score": 850},

        {"name": "Anjali", "score": 800}
    ]

    return render_template(
        'leaderboard.html',
        players=players
    )


@app.route('/player/<name>')
def player(name):

    return render_template(
        'player.html',
        name=name
    )


if __name__ == "__main__":
    app.run(debug=True)