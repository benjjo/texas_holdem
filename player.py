from ranker import Rankinator
from deck import *


class Player(Rankinator):
    """
        Player determines and records the best hand that the player has.

        Parameters
        ----------
        self.best_hand_and_kicker : tuple
            Stores the hand and the kicker. eg ['A♥', 'K♥', 'Q♥', 'J♥', 'T♥'], 'A♥'
        self.hole_cards : list()
            Stores the hole cards. eg ['A♥', 'K♥']
        self.all_cards : dict()
            Holds the hole cards and the community cards and their respective ranks. eg
            {'K♥': 13, 'Q♥': 12, 'J♥': 11, 'T♥': 10, '9♠': 9, '2♠': 2, 'T♠': 10}
        self.best_hand_name = str()
            Holds the name of the best hand. eg 'Royal Flush'

    """
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
            self.all_cards.update({key: CARDS_MAP.get(key[0][0])})

    def get_cards_from_values(self, cards_list: list) -> list:
        # self.all_cards must be True
        list_of_cards = list()
        for value in cards_list:
            list_of_cards.append(list(self.all_cards.keys())[list(self.all_cards.values()).index(value)])

        return list_of_cards

    # Tools
    def get_Kicker(self, hole_cards: list) -> str:
        high_hole_card = self.convert_cards_to_integers(self.strip_suit(hole_cards))
        rank = max(high_hole_card)
        card = RANKS_MAP[rank]
        return card

    def get_best_hand_cards(self) -> list:
        print(self.best_hand_and_kicker[0])
        return self.best_hand_and_kicker[0]

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
        self.get_Kicker(hole_cards)
        self.set_best_hand_name(self.best_hand_and_kicker[0])

    def find_highest_straight(self, card_list: list) -> list:
        # Extract ranks and convert them to numeric values
        possible_ranks = self.strip_suit(card_list=card_list)
        possible_ranks = self.convert_cards_to_integers(possible_ranks)
        # Remove duplicates and sort the ranks as integers
        sorted_ranks = sorted(set(possible_ranks))

        # Variable to store the highest straight found
        highest_straight = []

        # Check for 5 consecutive numbers
        for i in range(len(sorted_ranks) - 4):
            # Check if 5 consecutive numbers form a straight
            if all(sorted_ranks[i + j] == sorted_ranks[i] + j for j in range(5)):
                current_straight = sorted_ranks[i:i + 5]

                # Update highest_straight if current_straight is higher
                if not highest_straight or current_straight[-1] > highest_straight[-1]:
                    highest_straight = current_straight

        return self.get_cards_from_values(highest_straight)  # Returns the highest straight found
