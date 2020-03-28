from api.models.card_holders import Game, Player

from api.game_states import JoinedGame, InvalidToken

from api.helpers import generate_token

from api.data import games

class JoinGame(object):
  def __init__(self, token, name):
    self.name = name
    self.token = token

  def perform(self):
    game = games.get_game(self.token)
    if not game:
      return (None, InvalidToken(self.token))
    code = generate_token([p.token for p in game.players])

    player = Player(self.name, code)
    game = game.including_new_player(player)
    state = JoinedGame(player.token, game.players)

    return (game, state)
