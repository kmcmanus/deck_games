games = {}

def save_game(game):
  #TODO lock on game code
  games[game.code] = game

def get_game(code):
  return games.get(code)

def get_game_codes():
  return games.keys()
