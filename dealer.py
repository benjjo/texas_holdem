import random
from deck import *


class Dealer:
    def __init__(self):
        self._burners = list()
        self._flop = list()
        self._turn = str()
        self._river = str()

    # Setters
    def set_burner(self, card: str) -> None:
        self._burners.append(card)
    # Setters and getters

    def set_flop(self, card: str) -> None:
        self._flop.append(card)

    def set_turn(self, card: str) -> None:
        self._turn = card

    def set_river(self, card: str) -> None:
        self._river = card

    # Setters
    def get_burners(self) -> list:
        return self._burners

    def get_flop(self) -> list:
        return self._flop

    def get_turn(self) -> str:
        return self._turn

    def get_river(self) -> str:
        return self._river

    # Tools
    def shuffle_deck(self):
        burner_deck = DECK.copy()
        random.shuffle(burner_deck)
        return burner_deck

    def deal_out_cards_and_flop(self):
        pass
