from collections import Counter
from deck import *


class Rankinator:
    def __init__(self, hole_cards: list, community_cards: list):
        self.hole_cards = list()
        self.community_cards = list()
        self.all_cards = list()
        self.all_cards_ranked = list()
        self.best_hand = str()
        # self.update_cards_in_play(hole_cards, community_cards)

    # Setters and getters
    def set_hole_cards(self, cards_list: list) -> None:
        self.hole_cards = cards_list

    def set_community_cards(self, cards_list: list) -> None:
        self.community_cards = cards_list

    def set_all_cards(self, hole_cards: list, community_cards: list) -> None:
        self.all_cards = hole_cards + community_cards

    def set_all_cards_ranked(self, cards_list: list) -> None:
        self.all_cards_ranked = cards_list

    def set_best_hand(self, hand: str) -> None:
        self.best_hand = hand

    def update_cards_in_play(self, hole_cards: list, community_cards: list) -> None:
        self.set_hole_cards(hole_cards)
        self.set_community_cards(community_cards)
        self.set_all_cards(hole_cards, community_cards)

    # Work functions
    def strip_suit(self, card_list: list) -> list:
        suits = [f'{H}', f'{D}', f'{S}', f'{C}']
        stripped_cards = [''.join(c for c in s if c not in suits) for s in card_list]
        return stripped_cards if stripped_cards else card_list

    def filter_cards_by_suit(self, card_list: list, suit: str) -> list:
        # Returns a list of cards with the selected suit
        suited_cards = [card for card in card_list if card[-1] == suit]
        return suited_cards

    def store_cards_by_rank(self, cards_list: list) -> dict:
        pass

    def convert_cards_to_integers(self, cards_list: list) -> list:
        # cards must be a list that has been stripped of the suit.
        # Ace is duplicated to 1 and 14.
        # Returns a unique sorted integer list
        cards_list = ['10' if item == 'T' else item for item in cards_list]
        cards_list = ['11' if item == 'J' else item for item in cards_list]
        cards_list = ['12' if item == 'Q' else item for item in cards_list]
        cards_list = ['13' if item == 'K' else item for item in cards_list]
        cards_list = ['14' if item == 'A' else item for item in cards_list]
        cards_list = cards_list + ['1'] if '14' in cards_list else cards_list
        int_list = [int(x) for x in cards_list]
        int_list.sort()
        return list(set(int_list))

    # hole_cards evaluators
    def check_Royal_Flush(self, cards_list: list) -> bool:
        self.set_best_hand('Royal Flush')
        for suit in [H, D, C, S]:
            flush_deck = self.filter_cards_by_suit(cards_list, suit)
            if len(flush_deck) >= 5:
                return all(card in flush_deck for card in [f'T{suit}', f'J{suit}', f'Q{suit}', f'K{suit}', f'A{suit}'])
        return False

    def check_Straight_Flush(self, cards_list: list) -> bool:
        self.set_best_hand('Straight Flush')
        for suit in [H, D, C, S]:
            flush_deck = self.filter_cards_by_suit(cards_list, suit)
            if len(flush_deck) >= 5:
                return self.check_Straight(card_list=flush_deck)

    def check_Four_of_a_Kind(self, cards_list: list) -> bool:
        self.set_best_hand('Four of a kind')
        cards_list = self.strip_suit(card_list=cards_list)
        count = Counter(cards_list)
        quads = [item for item, count in count.items() if count == 4]
        return bool(quads)

    def check_Full_House(self, cards_list: list) -> bool:
        self.set_best_hand('Full house')
        cards_list = self.strip_suit(card_list=cards_list)
        count = Counter(cards_list)
        pairs = [item for item, count in count.items() if count == 2]
        triples = [item for item, count in count.items() if count == 3]
        pairs = triples if len(triples) > 1 else pairs
        return bool(pairs and triples)

    def check_Flush(self, cards_list: list) -> bool:
        self.set_best_hand('Flush')
        suits_list = list()
        [suits_list.append(s[-1]) for s in cards_list]
        count = Counter(suits_list)
        suited = [item for item, count in count.items() if count >= 5]
        return bool(suited)

    def check_Straight(self, card_list: list) -> bool:
        self.set_best_hand('Straight')
        # Extract ranks and convert them to numeric values
        possible_ranks = self.strip_suit(card_list=card_list)
        possible_ranks = self.convert_cards_to_integers(possible_ranks)
        # Remove duplicates and sort the ranks as integers
        sorted_ranks = sorted(set(possible_ranks))

        # Check for 5 consecutive numbers
        for i in range(len(sorted_ranks) - 4):
            if all(sorted_ranks[i + j] == sorted_ranks[i] + j for j in range(5)):
                return True
        return False

    def check_Three_of_a_Kind(self, cards_list: list) -> bool:
        self.set_best_hand('Three of a kind')
        # Creates a list with the triples. Checks list for length more than 0
        cards_list = self.strip_suit(card_list=cards_list)
        count = Counter(cards_list)
        triples = [item for item, count in count.items() if count == 3]
        return bool(triples)

    def check_Two_Pair(self, cards_list: list) -> bool:
        self.set_best_hand('Two Pair')
        # Creates a list with the pairs. Checks list for length of 2 or better.3
        cards_list = self.strip_suit(card_list=cards_list)
        count = Counter(cards_list)
        two_pairs = [item for item, count in count.items() if count == 2]
        return len(two_pairs) >= 2

    def check_One_Pair(self, cards_list: list) -> bool:
        self.set_best_hand('One Pair')
        # Creates a list with the pairs. Checks list for length of 1
        cards_list = self.strip_suit(card_list=cards_list)
        count = Counter(cards_list)
        one_pair = [item for item, count in count.items() if count == 2]
        return len(one_pair) == 1

    def check_highest_card(self, card_list: list) -> str:
        pass

    # Return the hand type
    def return_highest_hand(self, card_list: list):
        functions = [self.check_Royal_Flush,
                     self.check_Straight_Flush,
                     self.check_Four_of_a_Kind,
                     self.check_Full_House,
                     self.check_Flush,
                     self.check_Straight,
                     self.check_Three_of_a_Kind,
                     self.check_Two_Pair,
                     self.check_One_Pair]

        for func in functions:
            if func(card_list):  # Call each function and check if it returns True
                return True
        return False  # Default return if none return True

