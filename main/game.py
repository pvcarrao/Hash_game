import random
import sqlite3
from datetime import datetime
from uuid import uuid4


class Game:
    def __init__(self):
        self.table_name = "GAMES"
        self.database = "DATABASE.db"
        self.table_headers = "(game_id PRIMARY KEY, current_player, pos_0, pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8)"

    def execute_sql(self, sql):
        conn = sqlite3.connect(database=self.database)
        c = conn.cursor()
        c.execute(sql)
        # TODO: remover próximas 2 linhas, usada só para debugar
        c.execute("SELECT * FROM GAMES")
        print(c.fetchone())
        conn.commit()

    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS " + self.table_name + self.table_headers
        self.execute_sql(sql)

    def execute_sql(self, sql):
        conn = sqlite3.connect(database=self.database)
        c = conn.cursor()
        c.execute(sql)
        # TODO: remover próximas 2 linhas, usada só para debugar
        c.execute("SELECT * FROM GAMES")
        print(c.fetchone())
        conn.commit()

    def pos_to_sql_string(self, positions):
        sql_string = ""
        for pos in positions:
            sql_string = str(pos) + ", "
        return sql_string

    def new_game(self):
        game_id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        current_player = random.choice(["X", "O"])
        positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pos_string = self.pos_to_sql_string(positions)
        sql = f"INSERT INTO {self.table_name}{self.table_headers} VALUES({game_id}, {current_player}, {positions})"
        self.execute_sql(sql)
        response = [game_id, current_player]
        return response


Game().new_game()
