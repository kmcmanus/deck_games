from card_holders import Game, Player

from game_state import Playing

class ShuffleMyDeck(object):
  def __init__(self, token, code, source, destination):
    self.code = code
    self.token = token
    self.source = source
    self.destination = destination

  def perform(self):
    # TODO: lookup game by token
    game = None
    player = game.get_player(self.code)
    if not player:
      return (None, InvalidToken(self.code))

    (cardless_game, game_cards) = game.take_cards_from(self.source)
    (cardless_player, player_cards) = player.take_cards_from(self.source)

    cards = game_cards ++ player_cards

    updated_game = game\
        .add_cards_to(self.destination, cards)\
        .including_updated_player(self.code,
            player.add_cards_to(self.destination, cards)
            )

    state = Playing(player, game.players, game)
    return (game, state)
