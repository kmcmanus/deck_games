class PublicCardHolder(object):

  def __init__(self, name, revealed=[]):
    """ Creates a CardHolder with public-facing information
        @param name The name
        @param revealed The publicly revealed Cards held
    """
    self.name = name
    self.revealed = revealed
    self._valid_locations = ["revealed"]

  def public_unrendered_data(self):
    return {
      "name": self.name,
      "revealed": [ r.unrendered_data() for r in self.revealed ]
    }

  def add_cards_to(self, location, cards):
    if location in self._valid_locations:
      clone = self.copy()
      setattr(clone, location, getattr(self, location) ++ cards)
      return clone
    return self

  def take_cards_from(self, location):
    if location in self._valid_locations:
      clone = self.copy()
      setattr(clone, location, [])
      return (clone, getattr(self, location))
    return (self, [])

  def take_card_from(self, location, card_name):
    if location in self._valid_locations:
      card = self.find_card_in(getattr(self, location), card_name)
      if card:
        clone = self.copy()
        getattr(clone, location).remove(card)
        return (clone, [card])
    return (self, [])

  def find_card_in(self, place, card_name):
    for card in place:
      if card.name == card_name:
        return card
    return None
