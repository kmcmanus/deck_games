
class Card(object):
  def __init__(self, name, color='#FFF', text=''):
    self.name = name
    self.color = color
    self.text = text

  def unrendered_data(self):
    return {
      "name": self.name,
      "color": self.color,
      "text": self.text
    }
