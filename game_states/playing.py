
class Playing(GameState):
  def __init__(self, player, other_players, game_cards):
    self.player = player
    self.other_players = other_players
    self.game_cards = game_cards
