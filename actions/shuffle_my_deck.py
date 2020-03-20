from card_holders import Game, Player

from game_state import Playing

class ShuffleMyDeck(object):
  def __init__(self, token, code):
    self.code = code
    self.token = token

  def perform(self):
    # TODO: lookup game by token
    game = None
    player = game.get_player(self.code).shuffle_deck()
    game = game.with_updated_player(self.code, player)
    state = Playing(player, game.players, game)
    return (game, state)
