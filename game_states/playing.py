
class Playing(GameState):
  def __init__(self, player, other_players, game):
    self.player = player
    self.other_players = other_players
    self.game = game

  def unrendered_data(self):
    return {
      "player": self.player.unrendered_data(),
      "other_players": { op.name: op.public_unrendered_data() },
      "game_cards": game.public_unrendered_data()
    }
