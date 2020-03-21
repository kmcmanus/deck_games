from card_holders import Game, Player

from game_state import Playing

class Ping(object):
  def __init__(self, token, code):
    self.code = code
    self.token = token

  def perform(self):
    # TODO: lookup game by token
    game = None
    player = game.get_player(self.code)
    state = Playing(player, game.players, game)
    return (game, state)
