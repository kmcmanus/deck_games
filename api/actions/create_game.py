from models.card_holders import Game, Player

from game_states import CreatedGame, UnknownDeck

from data import DECK_LOOKUP, games

from helpers import generate_token

class CreateGame(object):
  def __init__(self, deck_name, player_name):
    self.deck_name = deck_name
    self.player_name = player_name

  def perform(self):
    deck = DECK_LOOKUP[self.deck_name]
    if not deck:
      return (None, UnknownDeck(self.deck_name))
    token = generate_token(games.get_game_codes())
    code = generate_token()

    player = Player(self.player_name, code)
    game = Game(token, player.token, [ player ], False, [], [], deck.cards)
    state = CreatedGame(token, player.token)

    return (game, state)
