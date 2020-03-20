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
