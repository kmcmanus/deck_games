from models.card_holders import Game, Player

from game_states import Playing, InvalidToken

from data import games

class Shuffle(object):
  def __init__(self, token, code, location):
    self.code = code
    self.token = token
    self.location = location

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    player = game.get_player(self.code)
    if not player:
      return (None, InvalidToken(self.code))

    updated_player = player.shuffle(self.location)
    updated_game = game\
        .shuffle(self.location)[0]\
        .including_updated_player(self.code, updated_player)

    state = Playing(updated_player, updated_game.players, updated_game)
    return (updated_game, state)
