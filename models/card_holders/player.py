from . import CardHolder
class Player(CardHolder):

  def __init__(self, name, code, revealed=[], deck=[], hand=[]):
    """ Creates a new player
        @param name The public name
        @param code The uniquely-identifying API code
        @param revealed The publicly revealed Cards held
        @param deck The privately held Cards no one is aware of
        @param hand The privately held Cards only the player is aware of
    """
    super().__init__(name, code, revealed, deck)
    self.hand = hand
    self._valid_locations += ["hand"]
    self._prefix = "player"

  def unrendered_data(self):
    return { **super().public_unrendered_data(), **{
        "code": self.token,
        "hand": [ h.unrendered_data() for h in self.hand ]
      }
    }

  def public_unrendered_data(self):
    return { **super().public_unrendered_data(), **{
        "hand_size": len(self.hand)
      }
    }
