
class Player(CardHolder):

  def __init__(self, name, token, revealed=[], deck=[], hand=[]):
    """ Creates a new player
        @param name The public name
        @param token The uniquely-identifying API token
        @param revealed The publicly revealed Cards held
        @param deck The privately held Cards no one is aware of
        @param hand The privately held Cards only the player is aware of
    """
    super().__init__(self, name, token, revealed, deck)
    self.hand = hand

  def unrendered_data(self):
    return self.public_unrendered_data() + {
        "token": self.token,
        "hand": [ h.unrendered_data() for h in self.hand ]
      }

  def take_card_from_hand(self, card):
    new_player = self.copy()
    new_player.hand.remove(card)
    return new_player

  def add_card_to_hand(self, card):
    new_player = self.copy()
    new_player.hand = new_player.hand + card
    return new_player
