from . import PublicCardHolder
class Game(PublicCardHolder):
  def __init__(self, code, leader_token, players, started, discard=[], revealed=[], deck=[]):
    """ Creates a new player
        @param name The public name
        @param code The uniquely-identifying API token
        @param leader_token The token of the creating Player
        @param players A list of Players in the game
        @param started Whether or not the game has started
        @param discard The cards that have been discard
        @param revealed The publicly revealed Cards held
        @param deck The privately held Cards no one is aware of
    """
    super().__init__('', code, revealed, deck)
    self.leader_token = leader_token
    self.started = started
    self.discard = discard
    self._valid_locations += "discard"

  def public_unrended_data(self):
    return super().public_unrendered_data() + {
      "discard": [ d.unrendered_data() for d in self.discard ]
    }

  def start(self):
    new_game = self.copy()
    new_game.started = True
    return new_game

  def including_new_player(self, new_player):
    new_game = self.copy()
    new_game.players = new_game.players + new_player
    return new_game

  def including_updated_player(self, player_code, new_player):
    new_game = self.copy()
    new_game.players = [ p if p.token != player_code else new_player ]
    return new_game
