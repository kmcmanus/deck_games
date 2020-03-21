from card_holders import Game, Player

from game_state import JoinedGame, InvalidToken

from helpers import generate_token

from data import games

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
    state = JoinedGame(player.code)

    return (game.including_new_player(player), state)
