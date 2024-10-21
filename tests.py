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

        # Check that there are 13 of each suit
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
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'T']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'J']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'Q']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'K']) == 4)
        self.assertTrue(len([n for n in self.deck if n[0:-1] == 'A']) == 4)

    def test_strip_suit(self):
        rank = Rankinator([], [])
        cards = [f'2{H}', f'5{D}', f'8{S}', f'T{C}', f'K{S}']

        # Test True: suits are stripped
        self.assertListEqual(rank.strip_suit(card_list=cards), ['2', '5', '8', 'T', 'K'], "Failed strip_suit - Test 1")

        # Test True: there is no change
        cards = ['2', '5', '8', 'T', 'K']
        self.assertListEqual(rank.strip_suit(card_list=cards), ['2', '5', '8', 'T', 'K'], "Failed strip_suit - Test 2")

        # Test True: Triples are stripped
        cards = [f'2{H}', f'2{D}', f'2{S}', f'2{C}', f'K{S}']
        self.assertListEqual(rank.strip_suit(card_list=cards), ['2', '2', '2', '2', 'K'], "Failed strip_suit - Test 1")

    def test_filter_cards_by_suit(self):
        rank = Rankinator([], [])
        cards = [f'2{D}', f'5{H}', f'8{S}', f'T{C}']

        # Test ListEqual: Only Hearts
        self.assertListEqual(rank.filter_cards_by_suit(card_list=cards, suit=H), [f'5{H}'],
                             "Failed filter_cards_by_suit - Test 1")

        # Test ListEqual: Only Diamonds
        self.assertListEqual(rank.filter_cards_by_suit(card_list=cards, suit=D), [f'2{D}'],
                             "Failed filter_cards_by_suit - Test 2")

        # Test ListEqual: Only Spades
        self.assertListEqual(rank.filter_cards_by_suit(card_list=cards, suit=S), [f'8{S}'],
                             "Failed filter_cards_by_suit - Test 3")

        # Test ListEqual: Only Clubs
        self.assertListEqual(rank.filter_cards_by_suit(card_list=cards, suit=C), [f'T{C}'],
                             "Failed filter_cards_by_suit - Test 4")

        # Test ListEqual: No suits of type
        cards = [f'2{D}', f'5{H}', f'8{S}', f'T{S}']
        self.assertListEqual(rank.filter_cards_by_suit(card_list=cards, suit=C), [],
                             "Failed filter_cards_by_suit - Test 5")

        # Test ListEqual: Only Hearts in hand, returns all
        cards = [f'2{H}', f'5{H}', f'8{H}', f'T{H}']
        self.assertListEqual(rank.filter_cards_by_suit(card_list=cards, suit=H), cards,
                             "Failed filter_cards_by_suit - Test 6")

    def test_convert_cards_to_integers(self):
        rank = Rankinator([], [])
        cards_in = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        cards_out = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        # Test True: No high cards
        self.assertEqual(rank.convert_cards_to_integers(cards_in),
                         cards_out, "Failed convert_cards_to_integers - Test 1")
        # Test True: No picture cards
        cards_in = ['2', '3', '4', '5', '6', '7', '8', '9', 'T']
        cards_out = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(rank.convert_cards_to_integers(cards_in),
                         cards_out, "Failed convert_cards_to_integers - Test 2")
        # Test True: No picture cards
        cards_in = ['A', 'A', 'A']
        cards_out = [1, 14]
        self.assertEqual(rank.convert_cards_to_integers(cards_in),
                         cards_out, "Failed convert_cards_to_integers - Test 3")

    # Test the Ranker class
    def test_one_pair(self):
        rank = Rankinator([], [])
        cards_list = [f'3{H}', f'3{D}', f'8{S}', f'T{S}', f'K{S}']

        # Test True: One pair present in list
        self.assertTrue(rank.check_One_Pair(cards_list), "Failed check_One_Pair - test 1")

        # Test False: No pair present in list
        cards_list = [f'2{H}', f'3{D}', f'8{S}', f'T{S}', f'K{S}']
        self.assertFalse(rank.check_One_Pair(cards_list), "Failed check_One_Pair - test 2")

        # Test False: Two pair present in list
        cards_list = [f'3{H}', f'3{D}', f'T{H}', f'T{S}', f'K{S}']
        self.assertFalse(rank.check_One_Pair(cards_list), "Failed check_One_Pair - test 3")

    def test_two_pair(self):
        rank = Rankinator([], [])
        cards_list = [f'3{D}', f'3{S}', f'T{H}', f'T{S}', f'K{S}']

        # Test True: Two pair present in list
        self.assertTrue(rank.check_Two_Pair(cards_list), "Failed check_Two_Pair - test 1")

        # Test False: Only 1 pair
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'T{S}', f'K{S}']
        self.assertFalse(rank.check_Two_Pair(cards_list), "Failed check_Two_Pair - test 2")

        # Test True: Three pair present in list
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'8{H}', f'K{S}', f'K{H}']
        self.assertTrue(rank.check_Two_Pair(cards_list), "Failed check_Two_Pair - test 3")

        # Test False: A pair and a triple
        cards_list = [f'3{D}', f'3{S}', f'T{S}', f'T{H}', f'T{D}']
        self.assertFalse(rank.check_Two_Pair(cards_list), "Failed check_Two_Pair - test 4")

    def test_three_of_a_kind(self):
        rank = Rankinator([], [])
        cards_list = [f'2{D}', f'3{S}', f'T{H}', f'T{S}', f'T{C}']

        # Test True: 3oaK present in list
        self.assertTrue(rank.check_Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 1")

        # Test False: Two pair
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'T{S}', f'T{H}']
        self.assertFalse(rank.check_Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 2")

        # Test False: 4oaK in list
        cards_list = [f'3{D}', f'3{S}', f'3{C}', f'3{H}', f'T{H}']
        self.assertFalse(rank.check_Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 3")

        # Test True: Boat in list
        cards_list = [f'3{D}', f'3{S}', f'3{C}', f'T{D}', f'T{H}']
        self.assertTrue(rank.check_Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 4")

        # Test False: Two pair in list
        cards_list = [f'3{D}', f'3{S}', f'8{C}', f'8{H}', f'T{H}']
        self.assertFalse(rank.check_Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 5")

        # Test False: One Pair in list
        cards_list = [f'3{D}', f'3{S}', f'8{C}', f'9{H}', f'T{H}']
        self.assertFalse(rank.check_Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 6")

    def test_straight(self):
        rank = Rankinator([], [])
        cards_list = [f'2', f'3', f'4', f'5', f'6', f'T', f'K']

        # Test True: Straight exists
        self.assertTrue(rank.check_Straight(cards_list), "Failed check_Straight - test 1")

        # Test False: No straight
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'T{S}', f'K{S}']
        self.assertFalse(rank.check_Straight(cards_list), "Failed check_Straight - test 2")

        # Test True: Straight exists with Ace as 1
        cards_list = [f'A{D}', f'2{S}', f'3{S}', f'4{S}', f'5{S}']
        self.assertTrue(rank.check_Straight(cards_list), "Failed check_Straight - test 3")

        # Test True: Straight exists with Ace as high card
        cards_list = [f'T{D}', f'J{S}', f'Q{S}', f'K{S}', f'A{S}']
        self.assertTrue(rank.check_Straight(cards_list), "Failed check_Straight - test 4")

    def test_flush(self):
        rank = Rankinator([], [])

        # Test True: flush exists for Hearts
        cards_list = [f'4{H}', f'5{H}', f'8{H}', f'T{H}', f'K{H}', f'4{S}', f'5{S}']
        self.assertTrue(rank.check_Flush(cards_list), "Failed check_Flush - test 1")

        # Test True: flush exists for Diamonds
        cards_list = [f'4{D}', f'5{D}', f'8{D}', f'T{D}', f'K{D}', f'4{H}', f'5{H}']
        self.assertTrue(rank.check_Flush(cards_list), "Failed check_Flush - test 2")

        # Test True: flush exists for Spades
        cards_list = [f'4{S}', f'5{S}', f'8{S}', f'T{S}', f'K{S}', f'4{H}', f'5{H}']
        self.assertTrue(rank.check_Flush(cards_list), "Failed check_Flush - test 3")

        # Test True: flush exists for Clubs
        cards_list = [f'4{C}', f'5{C}', f'8{C}', f'T{C}', f'K{C}', f'4{H}', f'5{H}']
        self.assertTrue(rank.check_Flush(cards_list), "Failed check_Flush - test 4")

        # Test False: No flush in hand
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'T{S}', f'K{S}', f'4{H}', f'5{H}']
        self.assertFalse(rank.check_Flush(cards_list), "Failed check_Flush - test 5")

    def test_check_Full_House(self):
        rank = Rankinator([], [])

        # Test True: Boat exists
        cards_list = [f'4{H}', f'4{D}', f'4{C}', f'T{H}', f'T{D}', f'9{S}', f'2{S}']
        self.assertTrue(rank.check_Full_House(cards_list), "Failed check_Full_House - test 1")

        # Test False: Boat doesn't exist
        cards_list = [f'4{H}', f'4{D}', f'5{C}', f'T{H}', f'T{D}', f'9{S}', f'2{S}']
        self.assertFalse(rank.check_Full_House(cards_list), "Failed check_Full_House - test 2")

        # Test True: Two triples in hand
        cards_list = [f'4{H}', f'4{D}', f'4{C}', f'T{H}', f'T{D}', f'T{S}', f'2{S}']
        self.assertTrue(rank.check_Full_House(cards_list), "Failed check_Full_House - test 3")

    def test_check_Four_of_a_Kind(self):
        rank = Rankinator([], [])

        # Test True: Four of a kind exists
        cards_list = [f'4{H}', f'4{D}', f'4{C}', f'4{S}', f'T{D}', f'9{S}', f'2{S}']
        self.assertTrue(rank.check_Four_of_a_Kind(cards_list), "Failed check_Four_of_a_Kind - test 1")

        # Test False: Four of a kind not in the hand
        cards_list = [f'4{H}', f'4{D}', f'5{C}', f'T{H}', f'T{D}', f'9{S}', f'2{S}']
        self.assertFalse(rank.check_Four_of_a_Kind(cards_list), "Failed check_Four_of_a_Kind - test 2")

        # Test True: Four of a kind and three of a kind in the hand
        cards_list = [f'4{H}', f'4{D}', f'4{C}', f'4{S}', f'T{D}', f'T{S}', f'T{H}']
        self.assertTrue(rank.check_Four_of_a_Kind(cards_list), "Failed check_Four_of_a_Kind - test 3")

    def test_check_Straight_Flush(self):
        rank = Rankinator([], [])

        # Test True: Straight flush in hand
        cards_list = [f'5{H}', f'4{H}', f'6{H}', f'7{H}', f'8{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.check_Straight_Flush(cards_list), "Failed check_Straight_Flush - test 1")

        # Test False: No Straight flush in hand
        cards_list = [f'5{D}', f'4{H}', f'6{H}', f'7{H}', f'8{H}', f'9{S}', f'2{S}']
        self.assertFalse(rank.check_Straight_Flush(cards_list), "Failed check_Straight_Flush - test 2")

    def test_check_Royal_Flush(self):
        rank = Rankinator([], [])

        # Test True: Straight flush in hand
        cards_list = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.check_Royal_Flush(cards_list), "Failed check_Royal_Flush - test 1")

        # Test False: No Straight flush in hand
        cards_list = [f'A{S}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        self.assertFalse(rank.check_Royal_Flush(cards_list), "Failed check_Royal_Flush - test 2")

    def test_return_highest_hand(self):
        rank = Rankinator([], [])

        # Test True: Royal flush in hand
        cards_list = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 1.1")
        self.assertTrue(rank.best_hand == 'Royal Flush', "Failed return_highest_hand - test 1.2")

        # Test True: Straight flush in hand
        cards_list = [f'2{H}', f'3{H}', f'4{H}', f'5{H}', f'6{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 2.1")
        self.assertTrue(rank.best_hand == 'Straight Flush', "Failed return_highest_hand - test 2.2")

        # Test True: Four of a kind in hand
        cards_list = [f'A{H}', f'A{D}', f'A{S}', f'A{C}', f'T{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 3.1")
        self.assertTrue(rank.best_hand == 'Four of a kind', "Failed return_highest_hand - test 3.2")

        # Test True: full house in hand
        cards_list = [f'A{H}', f'A{D}', f'A{S}', f'T{D}', f'T{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 4.1")
        self.assertTrue(rank.best_hand == 'Full house', "Failed return_highest_hand - test 4.2")

        # Test True: flush in hand
        cards_list = [f'A{H}', f'9{H}', f'2{H}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 5.1")
        self.assertTrue(rank.best_hand == 'Flush', "Failed return_highest_hand - test 5.2")

        # Test True: Straight in hand
        cards_list = [f'3{D}', f'4{C}', f'5{H}', f'6{H}', f'7{H}', f'8{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 6.1")
        self.assertTrue(rank.best_hand == 'Straight', "Failed return_highest_hand - test 6.2")

        # Test True: Three of a kind in hand
        cards_list = [f'A{H}', f'A{D}', f'A{S}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 7.1")
        self.assertTrue(rank.best_hand == 'Three of a kind', "Failed return_highest_hand - test 7.2")

        # Test True: Two Pair in hand
        cards_list = [f'A{H}', f'A{D}', f'J{S}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 7.1")
        self.assertTrue(rank.best_hand == 'Two Pair', "Failed return_highest_hand - test 7.2")

        # Test True: Three of a kind in hand
        cards_list = [f'A{H}', f'A{D}', f'4{S}', f'J{H}', f'7{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.return_highest_hand(cards_list), "Failed return_highest_hand - test 7.1")
        self.assertTrue(rank.best_hand == 'One Pair', "Failed return_highest_hand - test 7.2")


# Run tests:
if __name__ == '__main__':
    unittest.main()
