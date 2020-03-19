import random
import sqlite3


class Game:
    def __init__(self):
        self.table_name = "GAMES"
        self.database = "DATABASE.db"

    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS " + self.table_name  + "(game_id, player, pos_x, pos_y)"
        self.execute_sql(sql)

    def execute_sql(self, sql):
        conn = sqlite3.connect(database=self.database)
        c = conn.cursor()
        c.execute(sql)
        # TODO: remover próximas 2 linhas, usada só para debugar
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

Game().create_table()

