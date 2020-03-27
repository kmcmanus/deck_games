from copy import copy
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

  def add_cards_to(self, full_location, cards):
    (prefix, location) = full_location.split("_")
    if prefix == self._prefix and location in self._valid_locations:
      clone = copy(self)
      setattr(clone, location, getattr(self, location) + cards)
      return clone
    return self

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

  def find_card_in(self, place, card_name):
    for card in place:
      if card.name == card_name:
        return card
    return None
