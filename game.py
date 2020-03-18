import random
import sqlite3


class Game:

    def new_game():
        database = sqlite3.connect("games.db")
        game_id = "1"
        player = random.choice(["X", "O"])
        response = [game_id, player]
        return response
