
class Game(PublicCardHolder):
  def __init__(self, code, leaderToken, players, started, max_player_count, discarded=[], revealed=[], deck=[]):
    super().__init__(self, '', code, revealed, deck)
    self.leader_token = leader_token
    self.started = started
    self.max_players = max_players
    self.discarded = discarded
