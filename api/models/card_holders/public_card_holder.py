from copy import copy
import random
from api.helpers import depy
class PublicCardHolder(object):

  def __init__(self, name, revealed=[]):
    """ Creates a CardHolder with public-facing information
        @param name The name
        @param revealed The publicly revealed Cards held
    """
    self.name = name
    self.revealed = revealed
    self._valid_locations = ["revealed"]
    self._prefix = "public"

  def public_unrendered_data(self):
    return {
      "name": self.name,
      "revealed": [ r.unrendered_data() for r in self.revealed ]
    }

  def find_card_in(self, place, card_name):
    for card in place:
      if card.name == card_name:
        return card
    return None

  def change_cards(self, full_location, func):
    (prefix, location) = full_location.split("_")
    if prefix == self._prefix and location in self._valid_locations:
      cards = getattr(self, location)
      clone = copy(self)
      changed = func(cards)
      setattr(clone, location, changed)
      return (clone, changed)
    return (self, [])

  def shuffle(self, full_location):
    return self.change_cards(full_location, depy(random.shuffle))

  def add_cards_to(self, full_location, cards):
    return self.change_cards(full_location, lambda c: c + cards)

  # TODO genericize the below into a 'remove_cards' function

  def take_cards_from(self, full_location):
    (prefix, location) = full_location.split("_")
    if prefix == self._prefix and location in self._valid_locations:
      clone = copy(self)
      setattr(clone, location, [])
      return (clone, getattr(self, location))
    return (self, [])

  def take_card_from(self, full_location, card_name):
    (prefix, location) = full_location.split("_")
    if prefix == self._prefix and location in self._valid_locations:
      card = self.find_card_in(getattr(self, location), card_name)
      if card:
        clone = copy(self)
        getattr(clone, location).remove(card)
        return (clone, [card])
    return (self, [])

  def draw_top_card(self, full_location):
    (prefix, location) = full_location.split("_")
    if prefix == self._prefix and location in self._valid_locations:
      cards = getattr(self, location)
      if len(cards) > 0:
        clone = copy(self)
        card = cards[-1]
        clone.deck = cards[:-1]
        return (clone, [card])
    return (self, [])
