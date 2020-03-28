from enum import Enum

class Location(Enum):
  LocalPlayArea = 1
  GlobalPlayArea = 2
  Discard = 3
  MyHand = 4
  PlayerDeck = 5
  GameDeck = 6
