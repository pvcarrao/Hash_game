import random
import sqlite3


class Game:
    def __init__(self):
        pass

    def create_database(self):
        conn = sqlite3.connect(database="database")
        c = conn.cursor()
        table_name = 'games'
        sql = 'create table if not exists ' + table_name + ' (id integer)'
        c.execute(sql)
        conn.commit()

    def new_game(self):
        game_id = "1"
        player = random.choice(["X", "O"])
        response = [game_id, player]
        return response

