from ranker import *
from deck import *
import unittest


class RankerTester(unittest.TestCase):

    # Test the deck constants
    def test_deck(self):
        self.deck = DECK.copy()
        # Check that we have a 52 card deck
        self.assertIs(52, len(self.deck))

        # Check that the deck is unique
        self.assertTrue(len(self.deck) == len(set(self.deck)))

        # Check that there are 13 of each suite
        self.assertTrue(len([s for s in self.deck if s[-1] == H]) == 13)
        self.assertTrue(len([s for s in self.deck if s[-1] == D]) == 13)
        self.assertTrue(len([s for s in self.deck if s[-1] == S]) == 13)
        self.assertTrue(len([s for s in self.deck if s[-1] == C]) == 13)

        # Check that there are 4 of each value
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '2']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '3']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '4']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '5']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '6']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '7']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '8']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '9']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == '10']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'J']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'Q']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'K']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'A']) == 4)

    # Test the Ranker class
    def test_one_pair(self):
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'2{D}', f'5{S}', f'8{S}', f'10{S}', f'K{S}']
        rank = Rankinator(hole_cards, community_cards)
        # Check one pair is True with first card
        self.assertTrue(rank.check_One_Pair(), "Failed One-pair check - test 1")

        # Check one pair is True with second card
        hole_cards = [f'3{S}', f'2{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertTrue(rank.check_One_Pair(), "Failed One-pair check - test 2")

        # Check two-pair fails
        hole_cards = [f'2{S}', f'K{D}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_One_Pair(), "Failed One-pair check - test 3")

        # Check three of a kind fails
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'2{D}', f'3{D}', f'2{H}', f'10{C}', f'K{C}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_One_Pair(), "Failed One-pair check - test 4")

        # Check that full house fails
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'2{D}', f'3{D}', f'3{D}', f'10{C}', f'K{C}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_One_Pair(), "Failed One-pair check - test 5")

        # Check no pair using cards in the hole_cards fails
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'4{D}', f'6{D}', f'7{D}', f'10{C}', f'K{C}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_One_Pair(), "Failed One-pair check - test 6")

        # Check no pair using cards in the hole_cards fails with a pair in the community_cards
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'4{D}', f'6{D}', f'7{D}', f'K{D}', f'K{C}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_One_Pair(), "Failed One-pair check - test 7")

    def test_two_pair(self):
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'2{D}', f'3{D}', f'8{S}', f'10{S}', f'K{S}']
        rank = Rankinator(hole_cards, community_cards)

        # Check Two pair is True with perfect cards
        self.assertTrue(rank.check_Two_Pair(), "Failed Two-pair check - test 1")

        # Check Two pair is False: Scenario 1: Your hole_cards Has a Pair, and the Board Has a Pair (No Two Pair)
        hole_cards = [f'2{S}', f'2{D}']
        community_cards = [f'3{D}', f'3{S}', f'8{S}', f'10{S}', f'K{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Two_Pair(), "Failed Two-pair check - test 2")

        # Check Two pair is False: Scenario 2: Your hole_cards Has a match, and the Board Has a Pair (No Two Pair)
        hole_cards = [f'8{S}', f'2{D}']
        community_cards = [f'3{D}', f'3{S}', f'8{S}', f'10{S}', f'K{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Two_Pair(), "Failed Two-pair check - test 3")

    def test_three_of_a_kind(self):
        hole_cards = [f'3{D}', f'3{S}']
        community_cards = [f'3{C}', f'2{D}', f'8{S}', f'10{S}', f'K{S}']
        rank = Rankinator(hole_cards, community_cards)

        # Check 3oaK is True with 2 in the hole_cards, one in the community
        self.assertTrue(rank.check_Three_of_a_Kind(), "Failed 3oaK check - test 1")

        # Check 3oaK is True with 1 in the hole_cards, 2 in the community
        hole_cards = [f'2{S}', f'3{D}']
        community_cards = [f'2{D}', f'2{C}', f'8{S}', f'10{S}', f'K{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertTrue(rank.check_Three_of_a_Kind(), "Failed 3oaK check - test 2")

        # Check 3oaK is False with 3 in the community
        hole_cards = [f'3{S}', f'3{D}']
        community_cards = [f'2{D}', f'2{C}', f'2{S}', f'10{S}', f'K{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Three_of_a_Kind(), "Failed 3oaK check - test 3")

        # Check 3oaK is False with 4oaK
        hole_cards = [f'3{S}', f'3{D}']
        community_cards = [f'3{H}', f'3{C}', f'2{S}', f'10{S}', f'K{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Three_of_a_Kind(), "Failed 3oaK check - test 4")

        # Check 3oaK is False with Full house
        hole_cards = [f'3{S}', f'3{D}']
        community_cards = [f'3{H}', f'2{C}', f'2{S}', f'10{S}', f'K{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Three_of_a_Kind(), "Failed 3oaK check - test 5")

    def test_straight(self):
        hole_cards = [f'3{D}', f'4{S}']
        community_cards = [f'5{C}', f'2{D}', f'6{S}', f'10{S}', f'K{S}']
        rank = Rankinator(hole_cards, community_cards)

        # Check straight is True with 2 in the hole_cards, 3 in the community
        self.assertTrue(rank.check_Straight(), "Failed straight check - test 1")

        # Check straight is False with 1 in the hole_cards, 4 in the community
        hole_cards = [f'2{S}', f'4{D}']
        community_cards = [f'2{D}', f'5{C}', f'6{S}', f'7{S}', f'8{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Straight(), "Failed straight check - test 2")

        # Check straight is False with 0 in the hole_cards, 5 in the community
        hole_cards = [f'2{S}', f'A{D}']
        community_cards = [f'4{D}', f'5{C}', f'6{S}', f'7{S}', f'8{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Straight(), "Failed straight check - test 3")

        # Check straight is True with [A,2] in the hole_cards, [3,4,5] in the community
        hole_cards = [f'2{S}', f'A{D}']
        community_cards = [f'3{D}', f'4{C}', f'5{S}', f'7{S}', f'8{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertTrue(rank.check_Straight(), "Failed straight check - test 4")

        # Check straight is True with a pair in the community_cards
        hole_cards = [f'2{S}', f'3{D}']
        community_cards = [f'3{C}', f'4{C}', f'5{S}', f'7{S}', f'6{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertTrue(rank.check_Straight(), "Failed straight check - test 5")

    def test_flush(self):
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'4{S}', f'5{S}', f'8{S}', f'10{S}', f'K{S}']
        rank = Rankinator(hole_cards, community_cards)

        # Test to see if flush exists
        self.assertTrue(rank.check_Flush())

        # Test to see if False when the hole_cards is different but the rest match
        hole_cards = [f'2{H}', f'3{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Flush())

        # Test to see if True when there are just enough to make the flush
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'4{H}', f'5{H}', f'8{S}', f'10{S}', f'K{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertTrue(rank.check_Flush())

        # Test to see if False when there aren't enough to make a flush
        hole_cards = [f'2{S}', f'3{S}']
        community_cards = [f'4{H}', f'5{H}', f'8{H}', f'10{S}', f'K{S}']
        rank.update_cards_in_play(hole_cards, community_cards)
        self.assertFalse(rank.check_Flush())

    def test_check_Full_House(self):
        pass

    def test_check_Four_of_a_Kind(self):
        pass

    def test_check_Straight_Flush(self):
        pass

    def test_check_Royal_Flush(self):
        pass


# Run tests:
if __name__ == '__main__':
    unittest.main()
