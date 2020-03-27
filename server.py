from flask import Flask, request
from data import games, decks
import actions
import json
import threading
import collections

app = Flask(__name__)

locks = collections.defaultdict(threading.Lock)

def resolve_action(action):
  token = getattr(action, 'token', 'new_game')
  with locks[token]:
    (game, state) = action.perform()
    if game:
      games.save_game(game)
    return state.render()

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/decks', methods=['GET'])
def get_decks():
  return json.dumps([d.name for d in decks.ALL_DECKS])

@app.route('/games/create/<deck>/<player>', methods=['POST'])
def create_game(deck, player):
  return resolve_action(actions.CreateGame(deck, player))

@app.route('/games/<token>/join/<name>', methods=['POST'])
def join_game(token, name):
  return resolve_action(actions.JoinGame(token, name))

@app.route('/games/<token>/start/<code>', methods=['POST'])
def start_game(token, code):
  return resolve_action(actions.StartGame(token, code))

@app.route('/games/<token>/ping/<code>', methods=['GET'])
def ping(token, code):
  return resolve_action(actions.Ping(token, code))

@app.route('/games/<token>/shuffle/<code>/<location>', methods=['POST'])
def shuffle_game_deck(token, code, location):
  return resolve_action(actions.Shuffe(token, code, location))

@app.route('/games/<token>/move/<code>/<source>/<destination>/all', methods=['POST'])
def move_cards(token, code, source, destination):
  return resolve_action(actions.MoveCards(token, code, source, destination))

@app.route('/games/<token>/move/<code>/<source>/<destination>/<card_name>', methods=['POST'])
def move_card(token, code, source, destination, card_name):
  return resolve_action(actions.MoveCard(token, code, card_name, source, destination))

@app.route('/games/<token>/give/<code>/<card_name>/<player_name>', methods=['POST'])
def give_card(token, code, card_name, player_name):
  return resolve_action(actions.GiveCard(token, code, card_name, player_name))

@app.route('/games/<token>/draw_card/<code>/<source>/<destination>', methods=['POST'])
def draw_player_card(token, code, source, destination):
  return resolve_action(actions.DrawCard(token, code, source, destination))
