from ranker import Rankinator
from deck import *


class Player(Rankinator):
    def __init__(self):
        super().__init__()
        self.best_hand_and_kicker = tuple()
        self.hole_cards = list()
        self.best_hand = str()
        self.all_cards = dict()

    # Setters and getters
    def set_hole_cards(self, cards_list: list) -> None:
        self.hole_cards = cards_list

    def set_best_hand_cards(self, cards: list) -> None:
        self.best_hand_and_kicker = (cards,'')

    def update_cards_in_play(self, hole_cards: list, community_cards: list) -> None:
        self.set_hole_cards(hole_cards)
        self.set_community_cards(community_cards)
        self.set_all_cards(hole_cards, community_cards)

    def set_best_hand(self, hand: str) -> None:
        self.best_hand = hand

    def set_all_cards(self, hole_cards: list, community_cards: list) -> None:
        card_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8,
                    '7': 7, '6':6, '5': 5, '4': 4, '3': 3, '2': 2}
        full_card_list = hole_cards + community_cards
        self.all_cards.clear()
        for key in full_card_list:
            self.all_cards.update({key: card_map.get(key[0][0])})

    # Tools
    def Kicker(self, hole_cards: list) -> bool:
        high_hole_card = self.convert_cards_to_integers(self.strip_suit(hole_cards))
        self.set_best_hand(RANKS[max(high_hole_card)])
        return False

    def get_best_hand_cards(self) -> tuple:
        return self.best_hand_and_kicker

    # Return the hand type
    def determine_highest_hand(self, card_list: list, hole_cards=None) -> bool:
        # Sets the name of the first hand matched in the list.
        hole_cards = card_list[0:2] if not hole_cards else hole_cards
        functions = [self.Royal_Flush,
                     self.Straight_Flush,
                     self.Four_of_a_Kind,
                     self.Full_House,
                     self.Flush,
                     self.Straight,
                     self.Three_of_a_Kind,
                     self.Two_Pair,
                     self.One_Pair]

        for func in functions:
            if func(card_list):  # Call each function and check if it returns True
                self.set_best_hand(func.__name__.replace('_', " "))
                return True

        self.Kicker(hole_cards)
        return False  # Default return if none return True
