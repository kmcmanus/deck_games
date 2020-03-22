from models import Deck, Card

# TODO add cards

grey = '#9E9E9E'

green = '#4CAF50'
red ='#F44336'
blue = '#2196F3'
purple = '#9C27B0'
yellow = '#FFEB3B'
orange = '#FF9800'

poker_ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
suits = [
    ('&#9824;', grey), # Spades, Grey
    ('&#9827;', green), # Clubs, Green
    ('&#9829;', red), # Hearts, Red
    ('&#9830;', blue), # Diamonds, Blue
  ]

skull_icon = '&#9760;'
flowers = [
  (green, '&#1421'),
  (red, '&#1758'),
  (blue, '&#3910'),
  (purple, '&#5814'),
  (yellow, '&#7360'),
  (orange, '&#8251')
]

coup = [
    Card("Cap", blue),
    Card("Ass", grey),
    Card("Con", red),
    Card("Amb", green),
    Card("Duk", purple)
] * 3

def skull_deck():
  for (color, icon) in flowers:
    flower = Card(icon, color)
    yield flower
    yield flower
    yield flower
    yield Card(skull_icon, color)


def make_suit(suit, ranks):
  (icon, color) = suit
  for rank in ranks:
    yield Card(str(rank) + icon, color)

def flatten(lol):
  return [i for l in lol for i in l]

POKER = Deck('Poker', flatten([make_suit(s, poker_ranks) for s in suits]))
COUP = Deck('Skull', skull_deck())
SKULL = Deck('Coup', coup)

ALL_DECKS = [ POKER, COUP, SKULL]

DECK_LOOKUP = { deck.name: deck for deck in ALL_DECKS }
