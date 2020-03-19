import flask
from flask import request, jsonify

from .main.game import Game

app = flask.Flask(__name__)
app.config["DEBUG"] = True

Game().create_database()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Bem vindo ao jogo da velha da galera </h1><p>Readme</p>"


@app.route('/game', methods=['POST'])
def new_game():
    resp = Game().new_game()
    return jsonify(resp)


@app.route('/game/{id}/movement', methods=['POST'])
def movement():
    # try:

    # except GameDoesNotExist:

    return

app.run()
