from . import PublicCardHolder
from copy import copy

class CardHolder(PublicCardHolder):

  def __init__(self, name, token, revealed=[], deck=[]):
    """ Creates a generic card holder
        @param name The public name
        @param token The uniquely-identifying API token
        @param revealed The publicly revealed Cards held
        @param deck The privately held Cards
    """
    super().__init__(name, revealed)
    self.token = token
    self.deck = deck
    self._valid_locations += "deck"

  def deck_size(self):
    """ Returns the size of the deck """
    return len(self.deck)

  def public_unrendered_data(self):
    return { **super().public_unrendered_data(), **{ "deck_size": self.deck_size() } }

  def draw_top_card(self):
    if len(self.deck) == 0:
      return (self, [])
    else:
      clone = copy(self)
      card = self.deck[-1]
      clone.deck = self.deck[:-1]
      return (self, [card])
