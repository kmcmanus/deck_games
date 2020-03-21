from models.card_holders import Game, Player

from game_states import Playing, InvalidToken

from data import games

class MoveCard(object):
  def __init__(self, token, code, card_name, source, destination):
    self.code = code
    self.token = token
    self.source = source
    self.destination = destination
    self.card_name = card_name

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    player = game.get_player(self.code)
    if not player:
      return (None, InvalidToken(self.code))

    (cardless_game, game_cards) = game.take_card_from(self.source, self.card_name)
    (cardless_player, player_cards) = player.take_card_from(self.source, self.card_name)

    cards = game_cards ++ player_cards

    updated_game = game\
        .add_cards_to(self.destination, cards)\
        .including_updated_player(self.code,
            player.add_cards_to(self.destination, cards)
            )

    state = Playing(player, game.players, game)
    return (game, state)
