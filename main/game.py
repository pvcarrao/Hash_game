import random
import sqlite3
import json
from datetime import datetime
from uuid import uuid4

from shared.exceptions import GameDoesNotExist, IncorrectPlayer
from shared.constants import (INCORRECT_PLAYER, MATCH_ENDED, RECORDED_MOVE, UNAVAILABLE_POSITION)

class Game:
    def __init__(self):
        self.table_name = "GAMES"
        self.database = "DATABASE.db"
        self.table_headers = "(game_id, current_player, positions)"
        self.winning_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def execute_sql(self, sql):
        """Execute an SQL command on local database
        Arguments:
            sql {str} -- ex: "CREATE TABLE IF NOT EXISTS GAMES(game_id, current_player, positions)"
        Returns:
            Selected items from database if using SELECT command on SQL command
            None if not using SELECT
        """
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
        """Converts a tuple of positions on the boar to an integer
        Arguments:
            tuple {tuple} -- ex: "summary_today"
        Returns:
            Selected items from database if using SELECT command on SQL command
            None if not using SELECT
        """
        converted_pos = tuple["x"] + 3*tuple["y"]
        return converted_pos

    def create_table(self):
        """Create database table if it does not exist
        Arguments:
            None
        Returns:
            None
        """
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name}{self.table_headers}"
        self.execute_sql(sql)

    def new_game(self):
        """Creates a new game in database
        Arguments:
            None
        Returns:
            dict with the new game basic data
        """
        game_id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        current_player = random.choice(["X", "O"])
        positions = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        json_positions = json.dumps(positions)
        sql = f"INSERT INTO {self.table_name}{self.table_headers} VALUES('{game_id}', '{current_player}', '{json_positions}')"
        self.execute_sql(sql)
        response = {"id": game_id, "first_player": current_player, "status_code": 200}
        return response

    def play_human(self, game_id, player, position_tuple):
        """Register a move from the user in the database
        Arguments:
            game_id {str} -- ex: "202003-1904-0540-3513d970-a741-46e9-9224-8705bebd89fc"
            player {str} -- ex: "X"
            position_tuple {tuple} -- ex: "{'x': 2, 'y': 2}"
        Returns:
            Response to frontend with the movement results
        """
        sql = f"SELECT * FROM {self.table_name} WHERE game_id = '{game_id}'"
        game = self.execute_sql(sql)
        if not game:
            raise GameDoesNotExist
        if game[0][1] != player:
            raise IncorrectPlayer
        current_positions = json.loads(game[0][2])
        if self.has_won(current_positions, "X"):
            response = {"msg": MATCH_ENDED, "winner": "X", "status_code": 200}
            return response
        elif self.has_won(current_positions, "O"):
            response = {"msg": MATCH_ENDED, "winner": "O", "status_code": 200}
            return response
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
            elif player == "O":
                sql = f"UPDATE {self.table_name} SET current_player = 'X' WHERE game_id = '{game_id}'"
                self.execute_sql(sql)  
            else:
                raise IncorrectPlayer             
            if self.has_won(current_positions, player):
                response = {"msg": MATCH_ENDED, "winner": player, "status_code": 200}
            elif len(available_pos) <= 1:
                response = {"msg": MATCH_ENDED, "winner": "Draw", "status_code": 200}
            else:
                response = {"msg": RECORDED_MOVE, "status_code": 200}
            return response
        else:
            response = {"msg": UNAVAILABLE_POSITION, "status_code": 204}
            return response

    def has_won(self, positions, player):
        """Checks if a player has won the game
        Arguments:
            player {str} -- ex: "X"
            positions {dict} -- ex: "{'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 'X'}"
        Returns:
            True if the player won.
            False if not.
        """
        for pos in self.winning_pos:
            if positions[str(pos[0])] == positions[str(pos[1])] == positions[str(pos[2])] == player:
                return True
        return False
