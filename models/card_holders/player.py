
class Player(CardHolder):

  def __init__(self, name, token, revealed=[], deck=[], hand=[]):
    super().__init__(self, name, token, revealed, deck)
    self.deck = deck
