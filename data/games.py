games = {}

def save_game(game):
  games[game.code] = game

def get_game(code):
  return games[code]

def get_game_codes():
  return games.keys()
