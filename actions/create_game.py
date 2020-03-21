from card_holders import Game, Player

from game_state import CreatedGame, InvalidDeck

from data import DECK_LOOKUP

from helpers import generate_token

class CreateGame(object):
  def __init__(self, name, deck_name, player_name):
    self.name = name
    self.deck_name = deck_name
    self.player_name = player_name

  def perform(self):
    deck = DECK_LOOKUP[self.deck_name]
    if not deck:
      return (None, UnknownDeck(self.deck_name))
    # todo get all existing tokens
    token = generate_token(game_tokens)
    code = generate_token()

    player = Player(self.player_name, code)
    game = Game(token, player.code, [ player ], false, [], [], deck)
    state = CreatedGame(token, player.code)

    return (game, state)
