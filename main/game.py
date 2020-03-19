import random
import sqlite3
import json
from datetime import datetime
from uuid import uuid4

from shared.exceptions import GameDoesNotExist
from shared.constants import (INCORRECT_PLAYER, MATCH_ENDED, RECORDED_MOVE, UNAVAILABLE_POSITION)

class Game:
    def __init__(self):
        self.table_name = "GAMES"
        self.database = "DATABASE.db"
        self.table_headers = "(game_id, current_player, positions)"
        self.winning_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def execute_sql(self, sql):
        conn = sqlite3.connect(database=self.database)
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        if "SELECT" in sql:
            selected = c.fetchall()
        else:
            selected = None
        conn.close
        if selected:
            return selected
    
    def pos_tuple_to_int(self, tuple):
        converted_pos = tuple["x"] + 3*tuple["y"]
        return converted_pos

    def create_table(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name}{self.table_headers}"
        self.execute_sql(sql)

    def new_game(self):
        game_id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        current_player = random.choice(["X", "O"])
        positions = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        json_positions = json.dumps(positions)
        sql = f"INSERT INTO {self.table_name}{self.table_headers} VALUES('{game_id}', '{current_player}', '{json_positions}')"
        self.execute_sql(sql)
        response = {"id": game_id, "first_player": current_player}
        return response

    def play_human(self, game_id, player, position_tuple):
        sql = f"SELECT * FROM {self.table_name} WHERE game_id = '{game_id}'"
        game = self.execute_sql(sql)
        if not game:
            raise GameDoesNotExist
        if game[0][1] != player:
            return {"msg": INCORRECT_PLAYER}
        current_positions = json.loads(game[0][2])
        available_pos = []
        for pos in range(9):
            if current_positions[str(pos)] == 0:
                available_pos.append(pos)
        position_number = self.pos_tuple_to_int(position_tuple)
        
        if position_number in available_pos:
            current_positions[str(position_number)] = player
            json_positions = json.dumps(current_positions)
            sql = f"UPDATE {self.table_name} SET positions = '{json_positions}' WHERE game_id = '{game_id}'"
            self.execute_sql(sql)
            if player == "X":
                sql = f"UPDATE {self.table_name} SET current_player = 'O' WHERE game_id = '{game_id}'"
                self.execute_sql(sql)
            else:
                sql = f"UPDATE {self.table_name} SET current_player = 'X' WHERE game_id = '{game_id}'"
                self.execute_sql(sql)              
            if self.has_won(current_positions, player):
                return {"msg": MATCH_ENDED, "winner": player}
            if available_pos.__le__ == 1:
                return {"msg": MATCH_ENDED, "winner": "Draw"}
            return {"msg": RECORDED_MOVE}
        else:
            return {"msg": UNAVAILABLE_POSITION}

    def has_won(self, positions, player):
        for pos in self.winning_pos:
            if positions[str(pos[0])] == positions[str(pos[1])] == positions[str(pos[2])] == player:
                return True
        return False
