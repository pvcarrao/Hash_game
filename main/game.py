import random
import sqlite3


class Game:
    def __init__(self):
        self.table_name = "games"

    def create_database(self):
        conn = sqlite3.connect(database="database")
        c = conn.cursor()
        sql = "create table if not exists " + self.table_name + " (id integer)"
        c.execute(sql)
        conn.commit()

    def execute_sql(self, sql):
        conn = sqlite3.connect(database="database")
        c = conn.cursor()
        c.execute(sql)
        conn.commit()

    def new_game(self):
        game_id = "1"
        player = random.choice(["X", "O"])
        response = [game_id, player]
        return response


