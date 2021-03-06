from . import PublicCardHolder

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
    self._valid_locations += ["deck"]
    self._prefix = "card_holder"

  def deck_size(self):
    """ Returns the size of the deck """
    return len(self.deck)

  def public_unrendered_data(self):
    return { **super().public_unrendered_data(), **{ "deck_size": self.deck_size() } }

