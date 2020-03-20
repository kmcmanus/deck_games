
class Card(object):
  def __init__(self, name, color='#FFF', text=''):
    """ Create a new card
        @param name The rendered name of the card
        @param color The HTML color this card should be rendered as
        @param text The additional text this card should be rendered with
    """
    self.name = name
    self.color = color
    self.text = text

  def unrendered_data(self):
    return {
      "name": self.name,
      "color": self.color,
      "text": self.text
    }
