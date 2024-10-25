from deck import *


class Dealer:
    def __init__(self):
        pass

    def shuffle_deck(self):
        burner_deck = DECK.copy()
        random.shuffle(burner_deck)
        return burner_deck
