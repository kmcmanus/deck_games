from card_holders import Game, Player

from game_state import JoinedGame

class JoinGame(object):
  def __init__(self, token, name):
    self.name = name
    self.token = token


  def perform(self):
    # TODO: lookup game by token
    # TODO: create player code

    game = None
    code = None

    player = Player(self.name, code)
    state = JoinedGame(player.code)

    return (game.including_new_player(player), state)
