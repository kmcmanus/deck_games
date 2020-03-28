
from api.models.card_holders import Game, Player

from api.game_states import Playing, InvalidToken

from api.data import games

class GiveCard(object):
  def __init__(self, token, code, source, card_name, recipient_name):
    self.token = token
    self.code = code
    self.source = source
    self.card_name = card_name
    self.recipient_name = recipient_name

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    player = game.get_player(self.code)
    if not player:
      return (None, InvalidToken(self.code))
    recipient = game.get_player_by_name(self.recipient_name)
    if not recipient:
      return (None, InvalidToken(self.recipient_name))

    (cardless_game, game_cards) = game.take_card_from(self.source, self.card_name)
    (cardless_player, player_cards) = player.take_card_from(self.source, self.card_name)

    cards = game_cards + player_cards

    carded_player = recipient.add_cards_to("player_hand", cards)[0]

    updated_game = cardless_game\
        .including_updated_player(cardless_player.token, cardless_player)\
        .including_updated_player(carded_player.token, carded_player)

    state = Playing(cardless_player, updated_game.players, updated_game)
    return (updated_game, state)
