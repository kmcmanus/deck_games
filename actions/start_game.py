from card_holders import Game, Player

from game_state import Playing, InvalidToken

from data import games

class StartGame(object):
  def __init__(self, token, code):
    self.token = token
    self.code = code


  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))

    if self.code != game.leader_token:
      return (None, InvalidToken(self.code))

    started_game = game.start()

    player = started_game.get_player(self.code)
    state = Playing(player, started_game.players, started_game)
    return (started_game, state)
