from collections import Counter
from deck import *


class Rankinator:
    def __init__(self):
        """
        Rankinator is a list of tools that are used to calculate the best hand that a
        player holds. It all comes down to determine_highest_hand().

        Parameters
        ----------
        self.hole_cards : list
            Cards held by player
        self.community_cards :  list
            The cards shared by all players
        self.all_cards : list
            Individual to each player. hole cards and community cards
        self.all_cards_ranked :  list
            A list of the integer ranks of all cards.
        self.best_hand : string
            The name of the best hand that the player holds
        self.best_hand_score :  integer
            Used to compare two hands by the Adjudicator class
        self.kicker_rank :  integer
            The rank of the kicker card held by the player
        """
        self.community_cards = list()
        self.best_hand_score = int()
        self.ace_high = bool()

    def reset_community_cards(self):
        self.community_cards = list()

    def update_community_cards(self, cards_list: list) -> None:
        self.community_cards += cards_list

    def set_best_hand_score(self, score: int) -> None:
        self.best_hand_score = score

    # Helper functions
    def strip_suit(self, card_list: list) -> list:
        """Helper function to Return a list of cards with the suit removed."""
        suits = [f'{H}', f'{D}', f'{S}', f'{C}']
        stripped_cards = [''.join(c for c in s if c not in suits) for s in card_list]
        return stripped_cards if stripped_cards else card_list

    def get_rank_and_suit(self, card: str) -> tuple:
        """Helper function to get the rank and suit from a card."""
        return tuple([card[0], card[-1]])

    def all_cards_in_list(self, list1: list, list2: list) -> bool:
        """Helper method that checks whether every element from list1 is present in list2.
        list1 = list containing the items to check.
        list2 = list with the items to be checked against.
        It returns True if all elements of list1 are in list2 and False otherwise."""
        return all(card in list2 for card in list1)

    def get_keys_with_matching_values(self, my_dict: dict, target_list: list) -> list:
        """Helper method: Get a key or list of keys from a dictionary, using a value or list of values.
        Uses list comprehension to get keys where values match items in target_list"""
        return [key for key, value in my_dict.items() if value in target_list]

    def filter_cards_by_suit(self, card_list: list, suit: str) -> list:
        # Returns a list of cards with the selected suit
        suited_cards = [card for card in card_list if card[-1] == suit]
        return suited_cards

    def get_highest_card(self, card_list: list) -> int:
        """Returns the highest card value in a list of cards.
            [f'2{H}', f'5{D}', f'8{S}', f'T{C}', f'K{S}'] will return 13"""
        # Step 1: Strip the suits from the card list
        stripped_cards = self.strip_suit(card_list)

        # Step 2: Convert stripped cards to integer values
        int_cards = self.convert_cards_to_integers(stripped_cards)

        # Step 3: Return the highest integer (card) in the list
        return max(int_cards) if int_cards else None

    def convert_cards_to_integers(self, cards_list: list) -> list:
        """cards must be a list that has been stripped of the suit.
        Ace is duplicated to 1 and 14.
        Returns a unique sorted integer list"""
        cards_list = ['10' if item == 'T' else item for item in cards_list]
        cards_list = ['11' if item == 'J' else item for item in cards_list]
        cards_list = ['12' if item == 'Q' else item for item in cards_list]
        cards_list = ['13' if item == 'K' else item for item in cards_list]
        cards_list = ['14' if item == 'A' else item for item in cards_list]
        cards_list = cards_list + ['1'] if '14' in cards_list else cards_list
        int_list = [int(x) for x in cards_list]
        int_list.sort()
        return list(set(int_list))

    def convert_card_to_integer(self, card: str) -> int:
        """Returns the value of the card in terms of a ranked integer. In the case that
        Ace refers to a low straight usage (ace_high == False), the value is 1. """
        substitutions = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'AL': 1}
        if 'A' in card and not self.ace_high:
            card = card.replace('A', 'AL')
        card = substitutions.get(card[:-1], card[:-1])
        return int(card)

    # hole_cards evaluators
    def Royal_Flush(self, cards_list: list) -> bool:
        for suit in [H, D, C, S]:
            flush_deck = self.filter_cards_by_suit(cards_list, suit)
            if len(flush_deck) >= 5:
                return all(card in flush_deck for card in [f'T{suit}', f'J{suit}', f'Q{suit}', f'K{suit}', f'A{suit}'])
        return False

    def Straight_Flush(self, cards_list: list) -> bool:
        for suit in [H, D, C, S]:
            flush_deck = self.filter_cards_by_suit(cards_list, suit)
            if len(flush_deck) >= 5:
                return self.Straight(card_list=flush_deck)

    def Four_of_a_Kind(self, cards_list: list) -> bool:
        cards_list = self.strip_suit(card_list=cards_list)
        count = Counter(cards_list)
        quads = [item for item, count in count.items() if count == 4]
        return bool(quads)

    def Full_House(self, cards_list: list) -> bool:
        cards_list = self.strip_suit(card_list=cards_list)
        count = Counter(cards_list)
        pairs = [item for item, count in count.items() if count == 2]
        triples = [item for item, count in count.items() if count == 3]
        pairs = triples if len(triples) > 1 else pairs
        return bool(pairs and triples)

    def Flush(self, cards_list: list) -> bool:
        suits_list = list()
        [suits_list.append(s[-1]) for s in cards_list]
        count = Counter(suits_list)
        suited = [item for item, count in count.items() if count >= 5]
        return bool(suited)

    def Straight(self, card_list: list) -> bool:
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

    def Three_of_a_Kind(self, cards_list: list) -> bool:
        # Creates a list with the triples. Checks list for length more than 0
        cards_list = self.strip_suit(card_list=cards_list)
        count = Counter(cards_list)
        triples = [item for item, count in count.items() if count == 3]
        return bool(triples)

    def Two_Pair(self, cards_list: list) -> bool:
        # Creates a list with the pairs. Checks list for length of 2 or better.3
        cards_list = self.strip_suit(cards_list)
        count = Counter(cards_list)
        two_pairs = [item for item, count in count.items() if count == 2]
        return len(two_pairs) >= 2

    def One_Pair(self, cards_list: list) -> bool:
        # Creates a list with the pairs. Checks list for length of 1
        cards_list = self.strip_suit(cards_list)
        count = Counter(cards_list)
        one_pair = [item for item, count in count.items() if count == 2]
        return len(one_pair) == 1

    def High_Card(self, cards_list: list) -> bool:

        return True
