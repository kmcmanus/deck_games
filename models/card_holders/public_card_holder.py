class PublicCardHolder(object):

  def __init__(self, name, revealed=[]):
    """ Creates a CardHolder with public-facing information
        @param name The name
        @param revealed The publicly revealed Cards held
    """
    self.name = name
    self.revealed_cards = revealed

  def public_unrendered_data(self):
    return {
      "name": self.name,
      "cards": [ r.unrendered_data() for r in self.revealed_cards ]
    }

  def without_revealed_cards(self):
    new_holder = self.copy()
    new_holder.revealed_cards = []
    return new_holder

  def take_cards_from(self, location):
    if location == "cards":
      return (self.revealed_cards, self.without_revealed_cards())
    return ([], self)

  def adding_revealed_cards(self, cards):
    new_holder = self.copy()
    new_holder.revealed_cards = self.revealed_cards ++ cards
    return new_holder

  def add_cards_to(self, location, cards):
    if location == "cards":
      return self.adding_revealed_cards(cards)
    return self
