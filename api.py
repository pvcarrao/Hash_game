import flask
from flask import request, jsonify

from main.game import Game
from exceptions import GameDoesNotExist
from constants import GAME_DOES_NOT_EXIST

app = flask.Flask(__name__)
app.config["DEBUG"] = True

Game().create_table()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Bem vindo ao jogo da velha da galera </h1><p>Readme</p>"


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
        return jsonify(GAME_DOES_NOT_EXIST)

app.run()
