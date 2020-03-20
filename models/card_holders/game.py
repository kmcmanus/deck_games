
class Game(PublicCardHolder):
  def __init__(self, code, leader_token, players, started, discarded=[], revealed=[], deck=[]):
    """ Creates a new player
        @param name The public name
        @param code The uniquely-identifying API token
        @param leader_token The token of the creating Player
        @param players A list of Players in the game
        @param started Whether or not the game has started
        @param discarded The cards that have been discarded
        @param revealed The publicly revealed Cards held
        @param deck The privately held Cards no one is aware of
    """
    super().__init__(self, '', code, revealed, deck)
    self.leader_token = leader_token
    self.started = started
    self.discarded = discarded

  def public_unrended_data(self):
    return super().public_unrendered_data() + {
      "discarded": [ d.unrendered_data() for d in self.discarded ]
    }

  def with_new_player(self, new_player):
    new_game = self.copy()
    new_game.players = new_game.players + new_player
    return new_game
