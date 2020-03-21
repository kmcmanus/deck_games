
class InvalidRequest(MessageState):
  pass

class InvalidToken(InvalidRequest):
  def __init__(self, token):
    self.token = token
    super().__init__(self, "The provided token is invalid.")

class DeckEmpty(InvalidRequest):
  def __init__(self):
    super().__init__(self, "The deck is empty")

class UnknownDeck(InvalidRequest):
  def __init__(self, deck):
    self.deck = deck
    super().__init__(self, "That is not a valid deck.")

class UnknownCard(InvalidRequest):
  def __init__(self, card):
    self.card = card
    super().__init__(self, "That is not a valid card.")

class UnknownLocation(InvalidRequest):
  def __init__(self, location):
    self.location = location
    super().__init__(self, "That is not a valid location.")
