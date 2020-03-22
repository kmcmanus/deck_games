from models.card_holders import Game, Player

from game_states import Playing, InvalidToken, GameNotStarted

from data import games

class Ping(object):
  def __init__(self, token, code):
    self.code = code
    self.token = token

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    if not game.started:
      return (None, GameNotStarted(game.players, game.leader()))
    player = game.get_player(self.code)
    state = Playing(player, game.players, game)
    return (None, state)
