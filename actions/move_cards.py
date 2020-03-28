from models.card_holders import Game, Player

from game_states import Playing, InvalidToken

from data import games

class MoveCards(object):
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

    (cardless_game, game_card) = game.take_cards_from(self.source)
    (cardless_player, player_card) = player.take_cards_from(self.source)

    cards = game_card + player_card

    updated_player = cardless_player.add_cards_to(self.destination, cards)[0]

    updated_game = cardless_game\
        .add_cards_to(self.destination, cards)[0]\
        .including_updated_player(self.code, updated_player)

    state = Playing(updated_player, updated_game.players, updated_game)
    return (updated_game, state)
