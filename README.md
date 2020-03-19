## Getting started

### 1. Install python 3.6.9

- Python 3.6.9

We recomend using Pyenv to manage your environment
[pyenv](https://github.com/pyenv/pyenv#installation).
pyenv-installer is also recomended
[pyenv-installer](https://github.com/pyenv/pyenv-installer)

```bash
# installing pyenv and python
curl https://pyenv.run | bash
exec $SHELL
pyenv install 3.6.9
```

### 2. Create a virtual environment and activate it.

```bash
# Using pyenv
pyenv virtualenv 3.6.9 venv-api
pyenv local venv-api
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```
### 4. Run the API

On the repository root directory:

```bash
python3 api.py
```

The API shoud be running now on http://localhost:5000/

## Using the API

Request:

http://127.0.0.1:5000/game - Method: POST

This request creates a new game on your local database and returns the game_id and the first player of the match.

http://127.0.0.1:5000/game/{{id}}/movement - Method: POST

You should send a game_id on the request url
And you should also send a body on the Post with a json and the following information: The player who is attempting to play and the coordinates of his move. Here is an example:

```bash
{
    "player": "O",
    "position": {
        "x": 2,
        "y": 2
    }
}
```

player can be "O" or "X" and positions range from 0 to 2, generating all 9 possibilities of the game.

The response will inform you about the result of the player's move.