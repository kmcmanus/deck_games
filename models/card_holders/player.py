
class Player(CardHolder):

  def __init__(self, name, token, revealed=[], deck=[], hand=[]):
    super().__init__(self, name, token, revealed, deck)
    self.deck = deck

  def unrendered_data(self):
    return self.public_unrendered_data() + {
        "token": self.token,
        "hand": [ h.unrendered_data() for h in hand ]
      }
