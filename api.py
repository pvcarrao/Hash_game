import flask
from flask import request, jsonify

from main.game import Game
from shared.exceptions import GameDoesNotExist, IncorrectPlayer
from shared.constants import GAME_DOES_NOT_EXIST, INCORRECT_PLAYER

app = flask.Flask(__name__)
app.config["DEBUG"] = True

Game().create_table()


@app.route('/game', methods=['POST'])
def new_game():
    resp = Game().new_game()
    return jsonify(resp)


@app.route('/game/<id>/movement', methods=['POST'])
def movement(id):
    data = request.json
    try:
        resp = Game().play_human(id, data["player"], data["position"])
        return jsonify(resp)    
    except GameDoesNotExist:
        response = {"msg": GAME_DOES_NOT_EXIST, "status_code": 404}
        return jsonify(response)
    except IncorrectPlayer:
        response = {"msg": INCORRECT_PLAYER, "status_code": 404}
        return jsonify(response)

app.run()
