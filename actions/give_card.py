
from card_holders import Game, Player

from game_state import Playing

class GiveCard(object):
  def __init__(self, token, code, card_name, recipient_name):
    self.token = token
    self.code = code
    self.card_name = card_name
    self.recipient_name = recipient_name

  def perform(self):
    # TODO: lookup game by token
    game = None
    player = game.get_player(self.code)
    if not player:
      return (None, InvalidToken(self.code))

    recipient = game.get_player_by_name(self.recipeint_name)
    if not recipient:
      return (None, InvalidToken(self.recipient_name))

    cards = [ c for c in player.hand if c.name == self.card_name ]

    if len(cards) == 0:
      return (None, UnknownCard(self.card_name))

    card = cards[0]

    cardless_player = player.take_card_from_hand(card)
    carded_player = recipient.add_card_to_hand(card)

    updated_game = game\
        .including_updated_player(cardless_player.code, cardless_player)\
        .including_updated_player(carded_player.code, carded_player)

    state = Playing(player, updated_game.players, updated_game)
    return (updated_game, state)
