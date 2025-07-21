import random
from deck import *


class Dealer:
    def __init__(self):
        self._burners = list()
        self._flop = list()
        self._turn = str()
        self._river = str()
        self._community_cards = list()
        self._deck = DECK.copy()

    # Setters
    def set_burner(self, card: str) -> None:
        self._burners.append(card)

    def set_flop(self, card: str) -> None:
        self._flop.append(card)

    def set_turn(self, card: str) -> None:
        self._turn = card

    def set_river(self, card: str) -> None:
        self._river = card

    def set_community_cards(self, card: str) -> None:
        self._community_cards.append(card)

    def clear_community_cards(self) -> None:
        self._community_cards = list()

    # Getters
    def get_burners(self) -> list:
        return self._burners

    def get_flop(self) -> list:
        return self._flop

    def get_turn(self) -> str:
        return self._turn

    def get_river(self) -> str:
        return self._river

    def get_deck(self) -> list:
        return self._deck

    def get_community_cards(self) -> list:
        return self._community_cards

    def new_deck(self) -> None:
        self._burners = list()
        self._flop = list()
        self._turn = str()
        self._river = str()
        self._community_cards = list()
        self._deck = DECK.copy()
        random.shuffle(self._deck)

    # Tools
    def shuffle_deck(self):
        return random.shuffle(self.get_deck())

    def deal_out_cards_and_flop(self, players, game):
        for card_count in range(2):
            for person in players:
                game.get_player(person).set_pocket_card(self._deck.pop())
        # Burn a card
        self.set_burner(self._deck.pop())
        # Deal out the Flop.
        for card_count in range(3):
            card = self._deck.pop()
            self.set_flop(card)
            self._community_cards.append(card)

    def deal_out_a_single_card(self):
        # Burn a card
        self.set_burner(self._deck.pop())
        # Deal out the Turn/River.
        # Update the community cards
        if self.get_turn():
            self.set_river(self._deck.pop())
            self._community_cards.append(self.get_river())
        else:
            self.set_turn(self._deck.pop())
            self._community_cards.append(self.get_turn())

    def run_it_again(self):
        # Burn a card
        self.set_burner(self._deck.pop())
        self.clear_community_cards()
        for i in range(5):
            self.set_community_cards(self._deck.pop())



