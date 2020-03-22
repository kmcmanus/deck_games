import threading
games = {}

lock = threading.Lock()

def save_game(game):
  with lock:
    games[game.token] = game

def get_game(token):
  return games.get(token)

def get_game_codes():
  return games.keys()
