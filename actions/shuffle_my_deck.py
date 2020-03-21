from models.card_holders import Game, Player

from game_states import Playing, InvalidToken

from data import games

class ShuffleMyDeck(object):
  def __init__(self, token, code):
    self.code = code
    self.token = token

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    player = game.get_player(self.code).shuffle_deck()
    game = game.including_updated_player(self.code, player)
    state = Playing(player, game.players, game)
    return (game, state)
