
class CardHolder(PublicCardHolder):

  def __init__(self, name, token, revealed=[], deck=[]):
    """ Creates a generic card holder
        @param name The public name
        @param token The uniquely-identifying API token
        @param revealed The publicly revealed Cards held
        @param deck The privately held Cards
    """
    super().__init__(self, name, revealed)
    self.token = token
    self.deck = deck

  def deck_size(self):
    """ Returns the size of the deck """
    return len(deck)

  def public_unrendered_data(self):
    return super().public_unrendered_data() + {
      "deck_size": self.deck_size
    }

  def without_deck(self):
    new_holder = self.copy()
    new_holder.deck = []
    return new_holder

  def take_cards_from(self, location):
    if location == "deck":
      return (self.deck, self.without_deck())
    return super().take_cards_from(self, location)

  def adding_deck_cards(self, cards):
    new_holder = self.copy()
    new_holder.deck = self.deck ++ cards
    return new_holder

  def add_cards_to(self, location, cards):
    if location == "deck":
      return self.adding_deck_cards(cards)
    return super().add_cards_to(self, location, cards)
