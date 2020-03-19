class PublicCardHolder(object):

  def __init__(self, name, revealed=[]):
    self.name = name
    self.revealed_cards = revealed

  def deck_size(self):
    return 0
