import json

class GameState(object):
  def render(self):
    return json.dumps(self.unrendered_data())

class MessageState(GameState):
  def __init__(self, message):
    """ Create a new message state.
        @param message The message to render.
    """
    self.message = message

  def unrendered_data(self):
    return { "message": self.message }

class GameNotStarted(GameState):
  def __init__(self, players, leader):
    self.players = players
    self.leader = leader

  def unrendered_data(self):
    return {
        "state": "waiting",
        "players": [p.name for p in players],
        "leader": leader.name
      }

class JoinedGame(GameState):
  def __init__(self, code):
    """ State to send when a user has joined a game.
        @param code Their player-code for this game.
    """
    self.code = code

  def unrendered_data(self):
    return {
        "code": self.code,
        "message": "You have joined this game. Please stand by."
      }

class CreatedGame(GameState):
  def __init__(self, token, code):
    """ State to send when a user has joined a game.
        @param code Their player-code for this game.
    """
    self.code = code
    self.token = token

  def unrendered_data(self):
    return {
        "token": self.token,
        "code": self.code,
        "message": "You have created a game. Please share this token."
      }
