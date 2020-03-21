from card_holders import Game, Player

from game_state import JoinedGame

from helpers import generate_token

class JoinGame(object):
  def __init__(self, token, name):
    self.name = name
    self.token = token


  def perform(self):
    # TODO: lookup game by token
    game = None
    code = generate_token([p.token for p in game.players])

    player = Player(self.name, code)
    state = JoinedGame(player.code)

    return (game.including_new_player(player), state)
