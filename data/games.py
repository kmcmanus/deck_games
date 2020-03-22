import threading
games = {}

lock = threading.Lock()

def save_game(game):
  with lock:
    games[game.code] = game

def get_game(code):
  return games.get(code)

def get_game_codes():
  return games.keys()
