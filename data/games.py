import threading
games = {}


def save_game(game):
  games[game.token] = game

def get_game(token):
  return games.get(token)

def get_game_codes():
  return games.keys()
