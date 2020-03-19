import random
import sqlite3
import json
from datetime import datetime
from uuid import uuid4


class Game:
    def __init__(self):
        self.table_name = "GAMES"
        self.database = "DATABASE.db"
        self.table_headers = "(game_id, current_player, positions)"

    def execute_sql(self, sql):
        conn = sqlite3.connect(database=self.database)
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        if "SELECT" in sql:
            selected = c.fetchall()
        else:
            selected = None
        # TODO: remover duas próximas linhas
        c.execute(f"SELECT * FROM {self.table_name}")
        print(c.fetchall())

        conn.close
        if selected:
            return selected

    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS " + self.table_name + self.table_headers
        self.execute_sql(sql)

    def pos_to_sql_string(self, positions):
        sql_string = ""
        for pos in positions:
            sql_string = f"{sql_string}'{pos}', "
        return sql_string[:-2]

    def new_game(self):
        game_id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        current_player = random.choice(["X", "O"])
        positions = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        json_positions = json.dumps(positions)
        # pos_string = self.pos_to_sql_string(positions)
        sql = f"INSERT INTO {self.table_name}{self.table_headers} VALUES('{game_id}', '{current_player}', '{json_positions}')"
        self.execute_sql(sql)
        response = [game_id, current_player]
        return response

    def play_human(self, game_id, player, position):

        sql = f"SELECT * FROM {self.table_name} WHERE game_id = '{game_id}'"
        game = self.execute_sql(sql)
        if game[0] != game_id:
            return "Jogo inexistente"
        if game[1] != player:
            return "Jogador incorreto"
        positions = json.loads(game[2])
        
        # if not existe essa entrada na db:
        #     return "Jogo inexistente"
        # if player != current_player retornado da DB:
        #     return "jogador incorreto"
        # avaible_pos = construir avaible positions de acordo com as posições que são 0 na DB
        # if pos in self.available_pos:
        #     registrar mudança na DB da posição
        #     self.counter += (temos que pensar em como salvar esse counter)
        # else:
        #     return "Posição indisponível"



# TODO: remover proximas 3 linhas, sendo usadas só pra debugar
game_id = "202003-1901-0527-9bd78091-328e-4041-9df7-ee6fa4236a9c"
player = "X"
pos = [0, 0]
# Game().play_human