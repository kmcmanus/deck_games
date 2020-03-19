
class InvalidRequest(GameState):
  pass

class InvalidToken(InvalidRequest):
  pass

class DeckEmpty(InvalidRequest):
  pass

class UnknownCard(InvalidRequest):
  pass

class UnknownLocation(InvalidRequest):
  pass
