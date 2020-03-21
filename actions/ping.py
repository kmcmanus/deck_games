from card_holders import Game, Player

from game_state import Playing, InvalidToken

from data import games

class Ping(object):
  def __init__(self, token, code):
    self.code = code
    self.token = token

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    player = game.get_player(self.code)
    state = Playing(player, game.players, game)
    return (game, state)
