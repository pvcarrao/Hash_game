import random
import sqlite3
import json
from datetime import datetime
from uuid import uuid4

from exceptions import GameDoesNotExist
from constants import (INCORRECT_PLAYER, MATCH_ENDED, RECORDED_MOVE, UNAVAIBLE_POSITION)

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

    def new_game(self):
        game_id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        current_player = random.choice(["X", "O"])
        # TODO: criar o dict de positions de uma forma menos bruta
        positions = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        json_positions = json.dumps(positions)
        sql = f"INSERT INTO {self.table_name}{self.table_headers} VALUES('{game_id}', '{current_player}', '{json_positions}')"
        self.execute_sql(sql)
        response = [game_id, current_player]
        return response

    def play_human(self, game_id, player, position_tuple):

        sql = f"SELECT * FROM {self.table_name} WHERE game_id = '{game_id}'"
        game = self.execute_sql(sql)
        if not game:
            raise GameDoesNotExist
        if game[1] != player:
            return INCORRECT_PLAYER
        current_positions = json.loads(game[2])
        avaible_pos = []
        for pos in range(9):
            if current_positions[pos] == 0:
                avaible_pos.append = pos
        # TODO: converter a tupla em número da posição
        position_number = 0
        
        if position_number in avaible_pos:
            current_positions[position_number] = player
            json_positions = json.dumps(current_positions)
            sql = f"UPDATE {self.table_headers} SET positions = '{json_positions}' WHERE game_id = '{game_id}'"
            # TODO: check if has_won
            if has_won:
                return [MATCH_ENDED, player]
            return RECORDED_MOVE
        else:
            return UNAVAIBLE_POSITION




# TODO: remover proximas 3 linhas, sendo usadas só pra debugar
game_id = "202003-1901-0527-9bd78091-328e-4041-9df7-ee6fa4236a9c"
player = "X"
pos = [0, 0]
# Game().play_human