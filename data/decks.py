from models import Deck

# TODO add cards

POKER = Deck('Poker', [])
COUP = Deck('Coup', [])
SKULL = Deck('Skull', [])
LOVE_LETTER = Deck('Love Letter', [])

ALL_DECKS = [ POKER, COUP, SKULL, LOVE_LETTER]

DECK_LOOKUP = { deck.name: deck for deck in ALL_DECKS }
