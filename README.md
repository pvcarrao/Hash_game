## Getting started

### 1. Install python 3.6.9

- Python 3.6.9

Remember to also install pip.

We recomend using venv to manage your environment (Optional)

Linux (Debian/Ubuntu):
```bash
apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```bash
py -m venv venv
cd venv/Scripts
activate.bat
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

or you can install the requirements manually

```bash
pip install flask
```

### 3. Run the API

On the repository root directory:

Linux (Debian/Ubuntu):
```bash
python3 api.py
```

Windows:
```bash
py api.py
```

The API shoud be running now on http://localhost:5000/

## Using the API

POST: http://localhost:5000/game

This request creates a new game on your local database and returns the game_id and the first player of the match. Empty body.

POST: http://localhost:5000/game/{{id}}/movement

You should send a game_id on the request url.

You should also send a body on the Post with a json and the following information: The player who is attempting to play and the coordinates of his move. Here is an example:

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
