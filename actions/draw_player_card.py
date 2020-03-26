from models.card_holders import Game, Player

from game_states import Playing, InvalidToken, UnknownLocation

from data import games

class DrawPlayerCard(object):
  def __init__(self, token, code, destination):
    self.code = code
    self.token = token
    self.destination = destination

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    player = game.get_player(self.code)
    if not player:
      return (None, InvalidToken(self.code))

    (cardless_player, cards) = player.take_card_from("deck", self.card_name)

    updated_game = game\
        .add_cards_to(self.destination, cards)\
        .including_updated_player(self.code,
            cardless_player.add_cards_to(self.destination, cards)
            )

    state = Playing(player, game.players, game)
    return (game, state)
