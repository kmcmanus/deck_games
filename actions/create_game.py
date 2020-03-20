from card_holders import Game, Player

from game_state import CreatedGame

class CreateGame(object):
  def __init__(self, name, deck_name, player_name):
    self.name = name
    self.deck_name = deck_name
    self.player_name = player_name

  def perform(self):
    # TODO: lookup decks by name
    # TODO: create player code
    # TODO: generate token

    deck = None
    token = None
    code = None

    player = Player(self.player_name, code)
    game = Game(token, player.code, [ player ], false, [], [], deck)
    state = CreatedGame(token, player.code)

    return (game, state)
