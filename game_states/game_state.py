import json

class GameState(object):
  def render(self):
    return json.dumps(self.unrendered_data())

class MessageState(GameState):
  def __init__(self, message):
    self.message = message

  def unrendered_data(self):
    return { "message": self.message }

class GameNotStarted(MessageState):
  def __init__(self):
    super().__init__(self, "This game has not started yet.")

class GameEnded(MessageState):
  def __init__(self):
    super().__init__(self, "This game has ended.")

class GameFull(MessageState):
  def __init__(self):
    super().__init__(self, "This game is full.")

class JoinedGame(GameState):
  def __init__(self, code):
    self.code = code

  def unrendered_data(self):
    return {
        "code": self.code,
        "message": "You have joined this game. Please stand by."
      }
