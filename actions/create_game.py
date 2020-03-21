from card_holders import Game, Player

from game_state import CreatedGame, InvalidDeck

from data import DECK_LOOKUP

class CreateGame(object):
  def __init__(self, name, deck_name, player_name):
    self.name = name
    self.deck_name = deck_name
    self.player_name = player_name

  def perform(self):
    # TODO: create player code
    # TODO: generate token

    deck = DECK_LOOKUP[self.deck_name]
    if not deck:
      return (None, UnknownDeck(self.deck_name))
    token = None
    code = None

    player = Player(self.player_name, code)
    game = Game(token, player.code, [ player ], false, [], [], deck)
    state = CreatedGame(token, player.code)

    return (game, state)
