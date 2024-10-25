from ranker import Rankinator
from deck import *


class Player(Rankinator):
    def __init__(self):
        super().__init__()
        self.best_hand_and_kicker = tuple()
        self.hole_cards = list()
        self.all_cards = dict()
        self.best_hand_name = str()

    # Setters and getters
    def set_hole_cards(self, cards_list: list) -> None:
        self.hole_cards = cards_list

    def set_best_hand_name(self, name: str):
        self.best_hand_name = name

    def set_best_hand_and_kicker(self, hand_and_kicker: list) -> None:
        self.best_hand_and_kicker = (hand_and_kicker[0], hand_and_kicker[1])

    def update_cards_in_play(self, hole_cards: list, community_cards: list) -> None:
        self.set_hole_cards(hole_cards)
        self.set_community_cards(community_cards)
        self.set_all_cards(hole_cards, community_cards)

    def set_all_cards(self, hole_cards: list, community_cards: list) -> None:
        full_card_list = hole_cards + community_cards
        self.all_cards.clear()
        for key in full_card_list:
            self.all_cards.update({key: self.card_map.get(key[0][0])})

    # Tools
    def set_Kicker(self, hole_cards: list) -> None:
        high_hole_card = self.convert_cards_to_integers(self.strip_suit(hole_cards))
        rank = max(high_hole_card)
        card = RANKS_MAP[rank]
        self.set_best_hand_and_kicker([card, rank])

    def get_best_hand_cards(self) -> tuple:
        return self.best_hand_and_kicker

    # Return the hand type
    def determine_highest_hand(self, card_list: list, hole_cards=None) -> None:
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
                self.set_best_hand_name(func.__name__.replace('_', " "))
                return None

        self.set_Kicker(hole_cards)
        self.set_best_hand_name(self.best_hand_and_kicker[0])
