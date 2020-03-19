import random
import sqlite3


class Game:
    def __init__(self):
        self.table_name = "games"
        self.database = "database.db"

    def create_database(self):
        sql = "CREATE TABLE IF NOT EXISTS" + self.table_name  + "(game_id, player, pos_x, pos_y)"
        self.execute_sql

    def execute_sql(self, sql):
        conn = sqlite3.connect(database=self.database)
        c = conn.cursor()
        c.execute(sql)
        c.execute("SELECT * FROM GAMES")
        print(c.fetchone())
        conn.commit()

    def new_game(self):
        game_id = "1"
        player = random.choice(["X", "O"])
        response = [game_id, player]
        return response

    def new_game(self):
        database = sqlite3.connect("games.db")
        cursor = database.cursor()

Game().create_database()

