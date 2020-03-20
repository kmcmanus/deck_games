class PublicCardHolder(object):

  def __init__(self, name, revealed=[]):
    self.name = name
    self.revealed_cards = revealed

  def deck_size(self):
    return 0

  def public_unrendered_data(self):
    return {
      "deck_size": self.deck_size,
      "name": self.name,
      "cards": [ r.unrendered_data() for r in self.revealed_cards ]
    }
