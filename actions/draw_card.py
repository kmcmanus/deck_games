from models.card_holders import Game, Player

from game_states import Playing, InvalidToken, UnknownLocation

from data import games

class DrawCard(object):
  def __init__(self, token, code, source, destination):
    self.code = code
    self.token = token
    self.source = source
    self.destination = destination

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    player = game.get_player(self.code)
    if not player:
      return (None, InvalidToken(self.code))

    (cardless_game, game_cards) = game.draw_top_card(self.source)
    (cardless_player, player_cards) = player.draw_top_card(self.source)

    cards = game_cards + player_cards

    updated_player = cardless_player.add_cards_to(self.destination, cards)

    updated_game = cardless_game\
        .add_cards_to(self.destination, cards)\
        .including_updated_player(self.code, updated_player)

    state = Playing(updated_player, updated_game.players, updated_game)
    return (updated_game, state)
