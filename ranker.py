from collections import Counter


class Rankinator:
    def __init__(self, hole_cards: list, community_cards: list):
        self.hole_cards = list()
        self.hole_cards_ranks = list()
        self.hole_cards_ranks_numbered = list()  # Numbered lists are only to be utilised by straights.
        self.community_cards = list()
        self.hole_card_1 = str()
        self.hole_card_2 = str()
        self.community_ranks = list()
        self.all_cards = list()
        self.all_cards_ranks = list()
        self.all_cards_ranks_numbered = list()  # Numbered lists are only to be utilised by straights.
        self.update_cards_in_play(hole_cards, community_cards)

    # Setters and getters
    def set_hole_cards(self, hole_cards_list: list):
        self.hole_cards = hole_cards_list
        hole_cards = self.convert_cards_to_integers(self.strip_suit(self.hole_cards))
        self.hole_cards_ranks_numbered = hole_cards

    def set_community_cards(self, community_cards_list: list):
        self.community_cards = community_cards_list

    def set_card1(self, card: str):
        self.hole_card_1 = card

    def set_card2(self, card: str):
        self.hole_card_2 = card

    def set_hole_card_ranks(self, card1, card2):
        self.hole_cards_ranks = list()
        self.hole_cards_ranks = self.convert_cards_to_integers([card1, card2])

    def set_community_cards_numbers(self, numbers: list):
        self.community_ranks = numbers

    def set_all_cards(self, hole_cards_cards: list, community_cards_cards: list):
        self.all_cards = hole_cards_cards + community_cards_cards
        self.set_all_card_values(self.all_cards)

    def set_all_card_values(self, all_cards: list):
        # Strips the suite and leaves a list of values (not integers)
        self.all_cards_ranks = list()
        [self.all_cards_ranks.append(s[0:-1]) for s in all_cards]

    def set_all_cards_as_numbers(self):
        stripped_community_cards = self.strip_suit(self.community_cards)
        self.set_community_cards_numbers(self.convert_cards_to_integers(stripped_community_cards))
        self.all_cards_ranks_numbered = self.convert_cards_to_integers(self.all_cards_ranks)

    # Work functions
    def strip_suit(self, card_list: list):
        stripped_cards = list()
        [stripped_cards.append(s[0:-1]) for s in card_list]
        return stripped_cards

    def convert_cards_to_integers(self, cards: list):
        # cards must be a list that has been stripped of the suit.
        # Converts the all_card_values to integers.
        # Ace is duplicated to 1 and 14.
        # Sorts the list and returns a set.
        cards = ['11' if item == 'J' else item for item in cards]
        cards = ['12' if item == 'Q' else item for item in cards]
        cards = ['13' if item == 'K' else item for item in cards]
        cards = ['14' if item == 'A' else item for item in cards]
        if '14' in cards:
            cards = cards + ['1']
        int_list = [int(x) for x in cards]
        int_list.sort()
        return list(int_list)

    def update_cards_in_play(self, hole_cards: list, community_cards: list):
        self.set_hole_cards(hole_cards)
        self.set_community_cards(community_cards)
        self.set_card1(hole_cards[0][0:-1])
        self.set_card2(hole_cards[1][0:-1])
        self.set_hole_card_ranks(self.hole_card_1, self.hole_card_2)
        self.set_all_cards(hole_cards, community_cards)
        self.set_all_cards_as_numbers()

    # hole_cards evaluators
    def check_Royal_Flush(self):
        return self.check_Straight_Flush() and all(num in self.all_cards_ranks for num in ['10', 'J', 'Q', 'K', 'A'])

    def check_Straight_Flush(self):
        return self.check_Straight() and self.check_Flush()

    def check_Four_of_a_Kind(self):
        count = Counter(self.all_cards_ranks)
        quads = [item for item, count in count.items() if count == 4]
        return bool(quads)

    def check_Full_House(self):
        count = Counter(self.all_cards_ranks)
        pairs = [item for item, count in count.items() if count == 2]
        triples = [item for item, count in count.items() if count == 3]
        pairs = True if len(triples) > 1 else pairs
        return bool(pairs and triples)

    def check_Flush(self, card_count=5):
        community_cards_suits = list()
        [community_cards_suits.append(s[-1]) for s in self.all_cards]
        count = Counter(community_cards_suits)
        suited = [item for item, count in count.items() if count >= card_count]
        return bool(suited)

    def check_Straight(self, length=5):
        sorted_lst = list(set(self.all_cards_ranks_numbered))
        # Check if there is a sequence of 5 consecutive numbers
        for i in range(len(sorted_lst)):
            straight = sorted_lst[i:i + length]
            # Need to account for the duplication of Ace
            # Here we decide if we can remove one of the numbers
            if (1 in self.hole_cards_ranks_numbered) and (14 in self.hole_cards_ranks_numbered):
                if all(num in self.all_cards_ranks_numbered for num in [2, 3, 4, 5]):
                    self.all_cards_ranks_numbered.remove(14)
                    self.hole_cards_ranks_numbered.remove(14)
                else:
                    self.all_cards_ranks_numbered.remove(1)
                    self.hole_cards_ranks_numbered.remove(1)
            # Check if both hole cards are part of the straight
            if all(straight[j] == straight[0] + j for j in range(len(straight))):
                # Now that we have matched a sequence, check if the hole cards are in the sequence
                if all(num in straight for num in self.hole_cards_ranks_numbered):
                    return True  # Found a straight with both hole cards
        return False  # No straight with both hole cards

    def check_Three_of_a_Kind(self):
        count = Counter(self.all_cards_ranks)
        triples = [item for item, count in count.items() if count == 3]
        return bool(triples)

    def check_Two_Pair(self) -> bool:
        count = Counter(self.all_cards_ranks)
        pairs = [item for item, count in count.items() if count == 2]
        return len(pairs) == 2

    def check_One_Pair(self) -> bool:
        return len(self.all_cards_ranks) > len(set(self.all_cards_ranks))
