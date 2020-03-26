from . import GameState

class Playing(GameState):
  def __init__(self, player, other_players, game_cards):
    """ Message to send when the game is ongoing.
        @param player The player being sent the message
        @param other_players The list of other players also in this game
        @param game_cards The cards revealed to all players
    """
    self.player = player
    self.other_players = other_players
    self.game_cards = game_cards

  def unrendered_data(self):
    return {
      "state": "playing",
      "player": self.player.unrendered_data(),
      "other_players": [ op.public_unrendered_data() for op in self.other_players ],
      "game_cards": self.game_cards.public_unrendered_data()
    }
