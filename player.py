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
            Holds the hole cards and the community cards and their respective ranks for this player. eg
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

    def set_best_hand_and_kicker(self, hand_cards: list, kicker: str) -> None:
        self.best_hand_and_kicker = (hand_cards, kicker)

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
        return self.best_hand_and_kicker[0]

    # Methods to return the best hand combination
    def find_highest_ranked_hand(self, card_list: list, hole_cards=None) -> None:
        """Send the community cards and Hole cards to this method to determine:
                - The name of the highest hand. Defaults to kicker if no hand exists.
                - Sets the highest card hand to self.best_hand_name
                - Sets the kicker"""
        hole_cards = card_list[0:2] if not hole_cards else hole_cards
        map_hand_to_function = {'Royal_Flush': self.find_royal_flush(),
                                'Straight_Flush': self.find_highest_straight_flush(),
                                'Four_of_a_Kind': self.find_four_of_a_kind(),
                                'Full_House': self.find_highest_boat(),
                                'Flush': self.find_highest_flush(),
                                'Straight': self.find_highest_straight(),
                                'Three_of_a_Kind': self.find_highest_three_of_a_kind(),
                                'Two_Pair': self.find_highest_two_pair(),
                                'One_Pair': self.find_highest_pair()}

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
                best_hand = map_hand_to_function.get(func.__name__)
                kicker = self.get_Kicker(hole_cards)
                self.set_best_hand_and_kicker(best_hand, kicker)
                return None

        # No hand matched so the kicker is set to the hand name
        kicker = self.get_Kicker(hole_cards)
        self.set_best_hand_and_kicker([kicker], kicker)
        self.set_best_hand_name(kicker)

    def find_royal_flush(self) -> list:
        """This method efficiently finds and returns royal flush from
        the available cards in self.all_cards."""
        # Define the required ranks for a Royal Flush
        royal_flush_ranks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

        # Organize cards by suit
        suits = {}
        for card, rank in self.all_cards.items():
            suit = card[-1]  # Last character represents the suit
            if suit not in suits:
                suits[suit] = {}
            suits[suit][card[:-1]] = rank  # Map rank to card without the suit part

        # Check each suit for a Royal Flush
        for suit, cards in suits.items():
            # Check if all Royal Flush ranks are present in this suit
            if all(rank in cards and cards[rank] == royal_flush_ranks[rank] for rank in royal_flush_ranks):
                # Return the list of card names for the Royal Flush
                return [f"{rank}{suit}" for rank in royal_flush_ranks.keys()]

        return []  # Return an empty list if no Royal Flush is found

    def find_highest_straight_flush(self) -> list:
        """This method efficiently finds and returns the highest straight flush from
        the available cards in self.all_cards."""
        # Step 1: Organize cards by suit
        suits = {}
        for card, rank in self.all_cards.items():
            _, suit = self.get_rank_and_suit(card)
            if suit not in suits:
                suits[suit] = []
            suits[suit].append((card, rank))

        # Step 2: For each suit, find the highest straight flush
        highest_straight_flush = []

        for suit, cards in suits.items():
            # Step 3: Sort cards by rank within the suit
            sorted_ranks = sorted(cards, key=lambda x: x[1])

            # Step 4: Check for a straight within the sorted ranks
            for i in range(len(sorted_ranks) - 4):
                current_straight = [sorted_ranks[i]]
                for j in range(1, 5):
                    # Check if next rank is consecutive
                    if sorted_ranks[i + j][1] == sorted_ranks[i][1] + j:
                        current_straight.append(sorted_ranks[i + j])
                    else:
                        break

                # If a 5-card straight is found, check if it's the highest
                if len(current_straight) == 5:
                    if not highest_straight_flush or current_straight[-1][1] > highest_straight_flush[-1][1]:
                        highest_straight_flush = current_straight

        # Return the highest straight flush as a list of card names
        return [card for card, _ in highest_straight_flush]

    def find_four_of_a_kind(self) -> list:
        """This method efficiently finds and returns the highest 4 of a kind from
        the available cards in self.all_cards."""
        # Step 1: Count occurrences of each rank
        rank_counts = {}
        for card, rank in self.all_cards.items():
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        # Step 2: Find the rank with exactly four occurrences
        four_of_a_kind_rank = None
        for rank, count in rank_counts.items():
            if count == 4:
                four_of_a_kind_rank = rank
                break

        # Step 3: If no Four of a Kind is found, return an empty list
        if four_of_a_kind_rank is None:
            return []

        # Step 4: Collect all cards of the Four of a Kind rank
        four_of_a_kind_cards = [card for card, rank in self.all_cards.items() if rank == four_of_a_kind_rank]

        return four_of_a_kind_cards

    def find_highest_boat(self) -> list:
        """This method efficiently finds and returns the highest full-house from
        the available cards in self.all_cards."""
        # Step 1: Count occurrences of each rank
        rank_counts = {}
        for card, rank in self.all_cards.items():
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        # Step 2: Identify ranks for three of a kind and a pair
        three_of_a_kind_rank = None
        pair_rank = None
        for rank, count in rank_counts.items():
            if count == 3:
                three_of_a_kind_rank = rank
            elif count == 2:
                pair_rank = rank

        # Step 3: Collect cards for the Full House
        full_house_cards = [
            card for card, rank in self.all_cards.items()
            if rank == three_of_a_kind_rank or rank == pair_rank
        ]

        return full_house_cards

    def find_highest_flush(self) -> list:
        """This method efficiently finds and returns the highest flush from
        the available cards in self.all_cards."""
        # Step 1: Organize cards by suit
        suits = {}
        for card, rank in self.all_cards.items():
            suit = card[-1]  # The last character represents the suit
            if suit not in suits:
                suits[suit] = []
            suits[suit].append((card, rank))

        # Step 2: Check each suit for a flush and find the highest one
        highest_flush = []

        for suit, cards in suits.items():
            # Only consider suits with 5 or more cards
            if len(cards) >= 5:
                # Sort cards by rank in descending order and take the top 5
                sorted_cards = sorted(cards, key=lambda x: x[1], reverse=True)
                current_flush = sorted_cards[:5]  # Take the top 5 cards for the flush

                # Update highest_flush if current_flush has a higher top card
                if not highest_flush or current_flush[0][1] > highest_flush[0][1]:
                    highest_flush = current_flush

        # Return the highest flush as a list of card names
        return [card for card, _ in highest_flush]

    def find_highest_straight(self) -> list:
        """This method efficiently finds and returns the highest straight from
        the available cards in self.all_cards."""
        # Extract ranks and convert them to numeric values
        possible_ranks = self.strip_suit(list(self.all_cards.keys()))
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

    def find_highest_three_of_a_kind(self) -> list:
        """This method efficiently finds and returns the highest Three of a Kind
        from the available cards in self.all_cards."""
        # Step 1: Count occurrences of each rank
        rank_counts = {}
        for card, rank in self.all_cards.items():
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        # Step 2: Identify the highest rank with exactly three occurrences
        three_of_a_kind_rank = None
        for rank, count in sorted(rank_counts.items(), reverse=True):
            if count == 3:
                three_of_a_kind_rank = rank
                break  # Exit loop once we find the highest three of a kind

        # Step 3: If no Three of a Kind is found, return an empty list
        if three_of_a_kind_rank is None:
            return []

        # Step 4: Collect the cards for the Three of a Kind rank
        three_of_a_kind_cards = [card for card, rank in self.all_cards.items() if rank == three_of_a_kind_rank]

        return three_of_a_kind_cards

    def find_highest_two_pair(self) -> list:
        """This method efficiently finds and returns the highest two pairs from
        the available cards in self.all_cards.
            This method assumes that two pairs already exist.
            If that assumption is not true, it may return unexpected results.
            If there are more than two cards of the same rank, this method will still
            only take two for the pair."""
        # Step 1: Count occurrences of each rank
        rank_counts = {}
        for card, rank in self.all_cards.items():
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        # Step 2: Identify ranks with exactly two occurrences and sort them
        pair_ranks = [rank for rank, count in rank_counts.items() if count == 2]
        pair_ranks = sorted(pair_ranks, reverse=True)  # Sort in descending order to get the highest pairs

        # Step 3: Take the top two ranks (highest two pairs)
        highest_two_pairs = pair_ranks[:2]

        # Step 4: Collect the cards for the highest two pairs
        two_pair_cards = [card for card, rank in self.all_cards.items() if rank in highest_two_pairs]

        return two_pair_cards

    def find_highest_pair(self) -> list:
        # Step 1: Count occurrences of each rank
        rank_counts = {}
        for card, rank in self.all_cards.items():
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        # Step 2: Identify ranks with exactly two occurrences (pairs)
        pair_ranks = [rank for rank, count in rank_counts.items() if count == 2]

        # Step 3: Find the highest rank among the pairs
        if pair_ranks:
            highest_pair_rank = max(pair_ranks)
        else:
            return []  # Return an empty list if no pairs are found

        # Step 4: Collect the cards for the highest pair
        highest_pair_cards = [card for card, rank in self.all_cards.items() if rank == highest_pair_rank]

        return highest_pair_cards
