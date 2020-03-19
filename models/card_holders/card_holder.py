
class CardHolder(PublicCardHolder):

  def __init__(self, name, token, revealed=[], deck=[]):
    super().__init__(self, name, revealed)
    self.token = token
    self.deck = deck

  def deck_size(self):
    return len(deck)
