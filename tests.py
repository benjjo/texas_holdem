from bookie import *
from player import *
from dealer import *
from adjudicator import *
from game_manager import *
import unittest
from collections import Counter


class HoldemTester(unittest.TestCase):

    # Test the deck constants
    def test_DECK(self):
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

    def test_RANKS_MAP(self):
        self.assertTrue(RANKS_MAP.get(1) == 'Ace', "Failed test_RANKS_MAP - Test 1")
        self.assertTrue(RANKS_MAP.get(2) == 'Two', "Failed test_RANKS_MAP - Test 2")
        self.assertTrue(RANKS_MAP.get(3) == 'Three', "Failed test_RANKS_MAP - Test 3")
        self.assertTrue(RANKS_MAP.get(4) == 'Four', "Failed test_RANKS_MAP - Test 4")
        self.assertTrue(RANKS_MAP.get(5) == 'Five', "Failed test_RANKS_MAP - Test 5")
        self.assertTrue(RANKS_MAP.get(6) == 'Six', "Failed test_RANKS_MAP - Test 6")
        self.assertTrue(RANKS_MAP.get(7) == 'Seven', "Failed test_RANKS_MAP - Test 7")
        self.assertTrue(RANKS_MAP.get(8) == 'Eight', "Failed test_RANKS_MAP - Test 8")
        self.assertTrue(RANKS_MAP.get(9) == 'Nine', "Failed test_RANKS_MAP - Test 9")
        self.assertTrue(RANKS_MAP.get(10) == 'Ten', "Failed test_RANKS_MAP - Test 10")
        self.assertTrue(RANKS_MAP.get(11) == 'Jack', "Failed test_RANKS_MAP - Test 11")
        self.assertTrue(RANKS_MAP.get(12) == 'Queen', "Failed test_RANKS_MAP - Test 12")
        self.assertTrue(RANKS_MAP.get(13) == 'King', "Failed test_RANKS_MAP - Test 13")
        self.assertTrue(RANKS_MAP.get(14) == 'Ace', "Failed test_RANKS_MAP - Test 14")
        self.assertTrue(RANKS_MAP.get(15) == 'One Pair', "Failed test_RANKS_MAP - Test 15")
        self.assertTrue(RANKS_MAP.get(16) == 'Two Pair', "Failed test_RANKS_MAP - Test 16")
        self.assertTrue(RANKS_MAP.get(17) == 'Three of a Kind', "Failed test_RANKS_MAP - Test 17")
        self.assertTrue(RANKS_MAP.get(18) == 'Straight', "Failed test_RANKS_MAP - Test 18")
        self.assertTrue(RANKS_MAP.get(19) == 'Flush', "Failed test_RANKS_MAP - Test 19")
        self.assertTrue(RANKS_MAP.get(20) == 'Full House', "Failed test_RANKS_MAP - Test 20")
        self.assertTrue(RANKS_MAP.get(21) == 'Four of a Kind', "Failed test_RANKS_MAP - Test 21")
        self.assertTrue(RANKS_MAP.get(22) == 'Straight Flush', "Failed test_RANKS_MAP - Test 22")
        self.assertTrue(RANKS_MAP.get(23) == 'Royal Flush', "Failed test_RANKS_MAP - Test 23")

    def test_HANDS_MAP(self):
        self.assertTrue(HANDS_MAP.get('Two') == 2, "Failed test_HANDS_MAP - Test 1")
        self.assertTrue(HANDS_MAP.get('Three') == 3, "Failed test_HANDS_MAP - Test 2")
        self.assertTrue(HANDS_MAP.get('Four') == 4, "Failed test_HANDS_MAP - Test 3")
        self.assertTrue(HANDS_MAP.get('Five') == 5, "Failed test_HANDS_MAP - Test 4")
        self.assertTrue(HANDS_MAP.get('Six') == 6, "Failed test_HANDS_MAP - Test 5")
        self.assertTrue(HANDS_MAP.get('Seven') == 7, "Failed test_HANDS_MAP - Test 6")
        self.assertTrue(HANDS_MAP.get('Eight') == 8, "Failed test_HANDS_MAP - Test 7")
        self.assertTrue(HANDS_MAP.get('Nine') == 9, "Failed test_HANDS_MAP - Test 8")
        self.assertTrue(HANDS_MAP.get('Ten') == 10, "Failed test_HANDS_MAP - Test 9")
        self.assertTrue(HANDS_MAP.get('Jack') == 11, "Failed test_HANDS_MAP - Test 10")
        self.assertTrue(HANDS_MAP.get('Queen') == 12, "Failed test_HANDS_MAP - Test 11")
        self.assertTrue(HANDS_MAP.get('King') == 13, "Failed test_HANDS_MAP - Test 12")
        self.assertTrue(HANDS_MAP.get('Ace') == 14, "Failed test_HANDS_MAP - Test 13")
        self.assertTrue(HANDS_MAP.get('One Pair') == 15, "Failed test_HANDS_MAP - Test 14")
        self.assertTrue(HANDS_MAP.get('Two Pair') == 16, "Failed test_HANDS_MAP - Test 15")
        self.assertTrue(HANDS_MAP.get('Three of a Kind') == 17, "Failed test_HANDS_MAP - Test 16")
        self.assertTrue(HANDS_MAP.get('Straight') == 18, "Failed test_HANDS_MAP - Test 17")
        self.assertTrue(HANDS_MAP.get('Flush') == 19, "Failed test_HANDS_MAP - Test 18")
        self.assertTrue(HANDS_MAP.get('Full House') == 20, "Failed test_HANDS_MAP - Test 19")
        self.assertTrue(HANDS_MAP.get('Four of a Kind') == 21, "Failed test_HANDS_MAP - Test 20")
        self.assertTrue(HANDS_MAP.get('Straight Flush') == 22, "Failed test_HANDS_MAP - Test 21")
        self.assertTrue(HANDS_MAP.get('Royal Flush') == 23, "Failed test_HANDS_MAP - Test 22")

    def test_CARDS_MAP(self):
        self.assertTrue(CARDS_MAP.get('A') == 14, "Failed test_CARDS_MAP - Test 1")
        self.assertTrue(CARDS_MAP.get('K') == 13, "Failed test_CARDS_MAP - Test 2")
        self.assertTrue(CARDS_MAP.get('Q') == 12, "Failed test_CARDS_MAP - Test 3")
        self.assertTrue(CARDS_MAP.get('J') == 11, "Failed test_CARDS_MAP - Test 4")
        self.assertTrue(CARDS_MAP.get('T') == 10, "Failed test_CARDS_MAP - Test 5")
        self.assertTrue(CARDS_MAP.get('9') == 9, "Failed test_CARDS_MAP - Test 6")
        self.assertTrue(CARDS_MAP.get('8') == 8, "Failed test_CARDS_MAP - Test 7")
        self.assertTrue(CARDS_MAP.get('7') == 7, "Failed test_CARDS_MAP - Test 8")
        self.assertTrue(CARDS_MAP.get('6') == 6, "Failed test_CARDS_MAP - Test 9")
        self.assertTrue(CARDS_MAP.get('5') == 5, "Failed test_CARDS_MAP - Test 10")
        self.assertTrue(CARDS_MAP.get('4') == 4, "Failed test_CARDS_MAP - Test 11")
        self.assertTrue(CARDS_MAP.get('3') == 3, "Failed test_CARDS_MAP - Test 12")
        self.assertTrue(CARDS_MAP.get('2') == 2, "Failed test_CARDS_MAP - Test 13")

    # Test dealer class
    def test_setters_and_getters(self):
        new_dealer = Dealer()
        flop_cards = [f'T{D}', f'5{H}', f'6{S}']
        turn_card = f'T{H}'
        river_card = f'A{D}'
        burners = [f'T{C}', f'5{C}', f'6{C}']
        community_cards = [f'T{D}', f'5{H}', f'6{S}', f'T{H}', f'A{D}']

        # Setters
        new_dealer.set_flop(flop_cards[0])
        new_dealer.set_flop(flop_cards[1])
        new_dealer.set_flop(flop_cards[2])
        new_dealer.set_turn(turn_card)
        new_dealer.set_river(river_card)
        new_dealer.set_burner(burners[0])
        new_dealer.set_burner(burners[1])
        new_dealer.set_burner(burners[2])
        new_dealer.set_community_cards(flop_cards[0])
        new_dealer.set_community_cards(flop_cards[1])
        new_dealer.set_community_cards(flop_cards[2])
        new_dealer.set_community_cards(turn_card)
        new_dealer.set_community_cards(river_card)

        # Test True
        self.assertTrue(Counter(new_dealer.get_flop()) == Counter([f'T{D}', f'5{H}', f'6{S}']),
                        "Failed test_setters_and_getters - test 1")
        self.assertTrue(new_dealer.get_turn() == turn_card,
                        "Failed test_setters_and_getters - test 2")
        self.assertTrue(new_dealer.get_river() == river_card,
                        "Failed test_setters_and_getters - test 3")
        self.assertTrue(Counter(new_dealer.get_burners()) == Counter([f'T{C}', f'5{C}', f'6{C}']),
                        "Failed test_setters_and_getters - test 4")
        self.assertTrue(Counter(new_dealer.get_community_cards()) == Counter(community_cards),
                        "Failed test_setters_and_getters - test 5")

    def test_new_deck(self):
        dealer = Dealer()

        # Test True
        self.assertTrue(len(dealer.get_deck()) == 52, "Failed test_new_deck - test 1")
        dealer.get_deck().pop()
        self.assertTrue(len(dealer.get_deck()) == 51, "Failed test_new_deck - test 2")
        dealer.new_deck()
        self.assertTrue(len(dealer.get_deck()) == 52, "Failed test_new_deck - test 3")

    def test_shuffle_deck(self):
        dealer = Dealer()
        sorted_deck = DECK.copy()
        shuffled_deck = dealer.shuffle_deck()
        self.assertTrue(shuffled_deck != sorted_deck and
                        shuffled_deck != sorted_deck[::-1],
                        "Failed test_shuffle_deck - test 1")

    def test_deal_out_cards_and_flop(self):
        game = GameManager()
        dealer = Dealer()
        dealer.new_deck()
        players = {'Alice', 'Bob', 'Charlie'}
        game.make_players(players)
        dealer.deal_out_cards_and_flop(players, game)

        # Test True
        self.assertTrue(len(dealer.get_deck()) == (52 - 6 - 1 - 3),
                        "Failed test_deal_out_cards_and_flop - test 1")
        dealer.new_deck()
        self.assertTrue(len(dealer.get_deck()) == 52,
                        "Failed test_deal_out_cards_and_flop - test 2")

    def test_deal_out_a_single_card(self):
        game = GameManager()
        dealer = Dealer()
        dealer.new_deck()
        players = {'Alice', 'Bob', 'Charlie'}
        game.make_players(players)

        # Test True
        dealer.deal_out_a_single_card()
        self.assertTrue(len(dealer.get_deck()) == (52 - 1 - 1),
                        "Failed deal_out_a_single_card - test 1")
        self.assertTrue(bool(dealer.get_turn()),
                        "Failed deal_out_a_single_card - test 2")
        self.assertFalse(bool(dealer.get_river()),
                         "Failed deal_out_a_single_card - test 3")
        dealer.deal_out_a_single_card()
        self.assertTrue(len(dealer.get_deck()) == (52 - 1 - 1 - 1 - 1),
                        "Failed deal_out_a_single_card - test 4")
        self.assertTrue(bool(dealer.get_turn()),
                        "Failed deal_out_a_single_card - test 5")
        self.assertTrue(bool(dealer.get_river()),
                        "Failed deal_out_a_single_card - test 6")

    # Test the Ranker class
    def test_set_community_cards(self):
        # reset_community_cards
        # update_community_cards

        ranker = Rankinator()
        cards = [f'2{H}', f'5{D}', f'8{S}']
        ranker.update_community_cards(cards)
        self.assertListEqual(ranker.community_cards, [f'2{H}', f'5{D}', f'8{S}'],
                             "Failed test_set_community_cards - Test 1")

        cards = [f'T{C}']
        ranker.update_community_cards(cards)
        self.assertListEqual(ranker.community_cards, [f'2{H}', f'5{D}', f'8{S}', f'T{C}'],
                             "Failed test_set_community_cards - Test 2")

        cards = [f'K{S}']
        ranker.update_community_cards(cards)
        self.assertListEqual(ranker.community_cards, [f'2{H}', f'5{D}', f'8{S}', f'T{C}', f'K{S}'],
                             "Failed test_set_community_cards - Test 3")

        ranker.reset_community_cards()
        self.assertListEqual(ranker.community_cards, [],
                             "Failed test_set_community_cards - Test 4")

    def test_set_best_hand_score(self):
        ranker = Rankinator()
        score = 100
        ranker.set_best_hand_score(score)
        self.assertTrue(isinstance(ranker.best_hand_score, int),
                        "Failed test_set_best_hand_score - Test 1")
        self.assertTrue(ranker.best_hand_score == 100,
                        "Failed test_set_best_hand_score - Test 2")

    def test_strip_suit(self):
        ranker = Rankinator()
        cards = [f'2{H}', f'5{D}', f'8{S}', f'T{C}', f'K{S}']

        # Test True: suits are stripped
        self.assertListEqual(ranker.strip_suit(card_list=cards), ['2', '5', '8', 'T', 'K'],
                             "Failed strip_suit - Test 1")

        # Test True: there is no change
        cards = ['2', '5', '8', 'T', 'K']
        self.assertListEqual(ranker.strip_suit(card_list=cards), ['2', '5', '8', 'T', 'K'],
                             "Failed strip_suit - Test 2")

        # Test True: Triples are stripped
        cards = [f'2{H}', f'2{D}', f'2{S}', f'2{C}', f'K{S}']
        self.assertListEqual(ranker.strip_suit(card_list=cards), ['2', '2', '2', '2', 'K'],
                             "Failed strip_suit - Test 3")

    def test_get_rank_and_suit(self):
        ranker = Rankinator()
        card_1 = f'2{H}'
        card_2 = f'5{D}'
        card_3 = f'8{S}'
        self.assertTrue(ranker.get_rank_and_suit(card_1) == ('2', f'{H}'),
                        "Failed test_get_rank_and_suit - Test 1")
        self.assertTrue(ranker.get_rank_and_suit(card_2) == ('5', f'{D}'),
                        "Failed test_get_rank_and_suit - Test 2")
        self.assertTrue(ranker.get_rank_and_suit(card_3) == ('8', f'{S}'),
                        "Failed test_get_rank_and_suit - Test 3")

    def test_all_cards_in_list(self):
        ranker = Rankinator()
        list_1 = [f'2{D}', f'3{S}', f'4{C}', f'5{S}', f'6{D}', f'7{S}', f'8{C}']
        list_2 = [f'2{D}', f'3{S}', f'4{C}', f'5{S}', f'6{D}']
        list_3 = [f'3{D}', f'3{S}', f'4{C}', f'5{S}', f'6{D}']
        self.assertTrue(ranker.all_cards_in_list(list_2, list_1),
                        "Failed test_all_cards_in_list - Test 1")
        self.assertFalse(ranker.all_cards_in_list(list_3, list_1),
                         "Failed test_all_cards_in_list - Test 2")

    def test_get_keys_with_matching_values(self):
        ranker = Rankinator()
        dict_1 = {f'2{D}': 2, f'3{S}': 3, f'4{C}': 4}
        list_1 = [2, 3, 4]
        list_1_out = [f'2{D}', f'3{S}', f'4{C}']
        list_2 = [2, 3, 5]
        list_2_out = [f'2{D}', f'3{S}']
        list_3 = [5, 6, 7]
        list_3_out = []
        self.assertListEqual(ranker.get_keys_with_matching_values(dict_1, list_1), list_1_out,
                             "Failed test_get_keys_with_matching_values - Test 1")
        self.assertListEqual(ranker.get_keys_with_matching_values(dict_1, list_2), list_2_out,
                             "Failed test_get_keys_with_matching_values - Test 2")
        self.assertListEqual(ranker.get_keys_with_matching_values(dict_1, list_3), list_3_out,
                             "Failed test_get_keys_with_matching_values - Test 3")

    def test_filter_cards_by_suit(self):
        rank = Rankinator()
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

    def test_get_highest_card(self):
        rankinator = Rankinator()

        # Test True
        high_card = rankinator.get_highest_card(card_list=[f'T{C}', f'K{S}'])
        self.assertTrue(high_card == 13, "Failed get_highest_card, test 1")

        # Test True
        high_card = rankinator.get_highest_card(card_list=[f'T{C}', f'A{S}'])
        self.assertTrue(high_card == 14, "Failed get_highest_card, test 2")

        # Test True
        high_card = rankinator.get_highest_card(card_list=[f'K{C}', f'K{S}'])
        self.assertTrue(high_card == 13, "Failed get_highest_card, test 3")

    def test_convert_cards_to_integers(self):
        rank = Rankinator()
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

    def test_convert_card_to_integer(self):
        rankinator = Rankinator()
        rankinator.ace_high = True
        cards_list = [f'2{D}', f'3{S}', f'4{C}', f'5{S}', f'6{D}', f'7{S}', f'8{C}', f'9{S}',
                      f'T{S}', f'J{S}', f'Q{C}', f'K{S}', f'A{S}']

        # Test True
        card_number = 2
        test_num = 1
        for card in cards_list:
            converted_card = rankinator.convert_card_to_integer(card)
            self.assertTrue(converted_card == card_number,
                            f"Failed convert_card_to_integer, test {test_num}")
            card_number += 1
            test_num += 1

        rankinator.ace_high = False
        # Test True
        self.assertTrue(rankinator.convert_card_to_integer(f'A{S}') == 1,
                        "Failed convert_card_to_integer, test 15")

    def test_Royal_Flush(self):
        rank = Rankinator()

        # Test True: Straight flush in hand
        cards_list = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.Royal_Flush(cards_list), "Failed check_Royal_Flush - test 1")

        # Test False: No Straight flush in hand
        cards_list = [f'A{S}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        self.assertFalse(rank.Royal_Flush(cards_list), "Failed check_Royal_Flush - test 2")

    def test_Straight_Flush(self):
        rank = Rankinator()

        # Test True: Straight flush in hand
        cards_list = [f'5{H}', f'4{H}', f'6{H}', f'7{H}', f'8{H}', f'9{S}', f'2{S}']
        self.assertTrue(rank.Straight_Flush(cards_list), "Failed check_Straight_Flush - test 1")

        # Test False: No Straight flush in hand
        cards_list = [f'5{D}', f'4{H}', f'6{H}', f'7{H}', f'8{H}', f'9{S}', f'2{S}']
        self.assertFalse(rank.Straight_Flush(cards_list), "Failed check_Straight_Flush - test 2")

    def test_Four_of_a_Kind(self):
        rank = Rankinator()

        # Test True: Four of a kind exists
        cards_list = [f'4{H}', f'4{D}', f'4{C}', f'4{S}', f'T{D}', f'9{S}', f'2{S}']
        self.assertTrue(rank.Four_of_a_Kind(cards_list), "Failed check_Four_of_a_Kind - test 1")

        # Test False: Four of a kind not in the hand
        cards_list = [f'4{H}', f'4{D}', f'5{C}', f'T{H}', f'T{D}', f'9{S}', f'2{S}']
        self.assertFalse(rank.Four_of_a_Kind(cards_list), "Failed check_Four_of_a_Kind - test 2")

        # Test True: Four of a kind and three of a kind in the hand
        cards_list = [f'4{H}', f'4{D}', f'4{C}', f'4{S}', f'T{D}', f'T{S}', f'T{H}']
        self.assertTrue(rank.Four_of_a_Kind(cards_list), "Failed check_Four_of_a_Kind - test 3")

    def test_Full_House(self):
        rank = Rankinator()

        # Test True: Boat exists
        cards_list = [f'4{H}', f'4{D}', f'4{C}', f'T{H}', f'T{D}', f'9{S}', f'2{S}']
        self.assertTrue(rank.Full_House(cards_list), "Failed check_Full_House - test 1")

        # Test False: Boat doesn't exist
        cards_list = [f'4{H}', f'4{D}', f'5{C}', f'T{H}', f'T{D}', f'9{S}', f'2{S}']
        self.assertFalse(rank.Full_House(cards_list), "Failed check_Full_House - test 2")

        # Test True: Two triples in hand
        cards_list = [f'4{H}', f'4{D}', f'4{C}', f'T{H}', f'T{D}', f'T{S}', f'2{S}']
        self.assertTrue(rank.Full_House(cards_list), "Failed check_Full_House - test 3")

    def test_Flush(self):
        rank = Rankinator()

        # Test True: flush exists for Hearts
        cards_list = [f'4{H}', f'5{H}', f'8{H}', f'T{H}', f'K{H}', f'4{S}', f'5{S}']
        self.assertTrue(rank.Flush(cards_list), "Failed check_Flush - test 1")

        # Test True: flush exists for Diamonds
        cards_list = [f'4{D}', f'5{D}', f'8{D}', f'T{D}', f'K{D}', f'4{H}', f'5{H}']
        self.assertTrue(rank.Flush(cards_list), "Failed check_Flush - test 2")

        # Test True: flush exists for Spades
        cards_list = [f'4{S}', f'5{S}', f'8{S}', f'T{S}', f'K{S}', f'4{H}', f'5{H}']
        self.assertTrue(rank.Flush(cards_list), "Failed check_Flush - test 3")

        # Test True: flush exists for Clubs
        cards_list = [f'4{C}', f'5{C}', f'8{C}', f'T{C}', f'K{C}', f'4{H}', f'5{H}']
        self.assertTrue(rank.Flush(cards_list), "Failed check_Flush - test 4")

        # Test False: No flush in hand
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'T{S}', f'K{S}', f'4{H}', f'5{H}']
        self.assertFalse(rank.Flush(cards_list), "Failed check_Flush - test 5")

    def test_Straight(self):
        rank = Rankinator()
        cards_list = [f'2', f'3', f'4', f'5', f'6', f'T', f'K']

        # Test True: Straight exists
        self.assertTrue(rank.Straight(cards_list), "Failed check_Straight - test 1")

        # Test False: No straight
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'T{S}', f'K{S}']
        self.assertFalse(rank.Straight(cards_list), "Failed check_Straight - test 2")

        # Test True: Straight exists with Ace as 1
        cards_list = [f'A{D}', f'2{S}', f'3{S}', f'4{S}', f'5{S}']
        self.assertTrue(rank.Straight(cards_list), "Failed check_Straight - test 3")

        # Test True: Straight exists with Ace as high card
        cards_list = [f'T{D}', f'J{S}', f'Q{S}', f'K{S}', f'A{S}']
        self.assertTrue(rank.Straight(cards_list), "Failed check_Straight - test 4")

    def test_Three_of_a_Kind(self):
        rank = Rankinator()
        cards_list = [f'2{D}', f'3{S}', f'T{H}', f'T{S}', f'T{C}']

        # Test True: 3oaK present in list
        self.assertTrue(rank.Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 1")

        # Test False: Two pair
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'T{S}', f'T{H}']
        self.assertFalse(rank.Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 2")

        # Test False: 4oaK in list
        cards_list = [f'3{D}', f'3{S}', f'3{C}', f'3{H}', f'T{H}']
        self.assertFalse(rank.Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 3")

        # Test True: Boat in list
        cards_list = [f'3{D}', f'3{S}', f'3{C}', f'T{D}', f'T{H}']
        self.assertTrue(rank.Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 4")

        # Test False: Two pair in list
        cards_list = [f'3{D}', f'3{S}', f'8{C}', f'8{H}', f'T{H}']
        self.assertFalse(rank.Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 5")

        # Test False: One Pair in list
        cards_list = [f'3{D}', f'3{S}', f'8{C}', f'9{H}', f'T{H}']
        self.assertFalse(rank.Three_of_a_Kind(cards_list), "Failed check_Three_of_a_Kind - test 6")

    def test_Two_Pair(self):
        rank = Rankinator()
        cards_list = [f'3{D}', f'3{S}', f'T{H}', f'T{S}', f'K{S}']

        # Test True: Two pair present in list
        self.assertTrue(rank.Two_Pair(cards_list), "Failed check_Two_Pair - test 1")

        # Test False: Only 1 pair
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'T{S}', f'K{S}']
        self.assertFalse(rank.Two_Pair(cards_list), "Failed check_Two_Pair - test 2")

        # Test True: Three pair present in list
        cards_list = [f'3{D}', f'3{S}', f'8{S}', f'8{H}', f'K{S}', f'K{H}']
        self.assertTrue(rank.Two_Pair(cards_list), "Failed check_Two_Pair - test 3")

        # Test False: A pair and a triple
        cards_list = [f'3{D}', f'3{S}', f'T{S}', f'T{H}', f'T{D}']
        self.assertFalse(rank.Two_Pair(cards_list), "Failed check_Two_Pair - test 4")

    def test_One_Pair(self):
        rank = Rankinator()
        cards_list = [f'3{H}', f'3{D}', f'8{S}', f'T{S}', f'K{S}']

        # Test True: One pair present in list
        self.assertTrue(rank.One_Pair(cards_list), "Failed check_One_Pair - test 1")

        # Test False: No pair present in list
        cards_list = [f'2{H}', f'3{D}', f'8{S}', f'T{S}', f'K{S}']
        self.assertFalse(rank.One_Pair(cards_list), "Failed check_One_Pair - test 2")

        # Test False: Two pair present in list
        cards_list = [f'3{H}', f'3{D}', f'T{H}', f'T{S}', f'K{S}']
        self.assertFalse(rank.One_Pair(cards_list), "Failed check_One_Pair - test 3")

    def test_High_Card(self):
        rank = Rankinator()

        # Test True: One pair present in list
        self.assertTrue(rank.High_Card([]), "Failed High_Card - test 1")

    # Test player class
    def test_set_pocket_card(self):
        player1 = Player(player_name='Player 1')
        card1 = f'9{H}'
        card2 = f'K{H}'
        player1.set_pocket_card(card1)
        player1.set_pocket_card(card2)
        # Test True
        self.assertTrue(card1 in player1._pocket_cards,
                        'Failed set_pocket_card - Test 1')
        self.assertTrue(card2 in player1._pocket_cards,
                        'Failed set_pocket_card - Test 2')
        self.assertTrue(len(player1._pocket_cards) == 2,
                        'Failed set_pocket_card - Test 3')

    def test_set_best_hand_name(self):
        player1 = Player(player_name='Player 1')
        player1.set_best_hand_name('Flush')
        # Test True
        self.assertTrue(player1._best_hand_name == 'Flush',
                        'Failed test_set_best_hand_name - Test 1')
        self.assertTrue(player1.ace_high,
                        'Failed test_set_best_hand_name - Test 2')

        player1.set_best_hand_name('Straight')
        self.assertTrue(player1._best_hand_name == 'Straight',
                        'Failed test_set_best_hand_name - Test 3')
        # Test False
        self.assertFalse(player1.ace_high,
                         'Failed test_set_best_hand_name - Test 4')

    def test_set_best_hand_and_kicker(self):
        player = Player(player_name='Player 1')

        # Test ListEqual: Royal Flush returned and not the lower suited
        hand = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}']
        kicker = f'A{H}'
        player.set_best_hand_and_kicker(hand, kicker)
        self.assertListEqual(player.get_best_hand_cards(), hand,
                             'Failed set_best_hand_cards - test 1')
        self.assertTrue(player._best_hand_and_kicker[1] == kicker,
                        'Failed set_best_hand_cards - test 2')

    def test_set_all_cards(self):
        player = Player(player_name='Player 1')

        # Test True: Royal flush in hand
        hole_cards: list[str] = [f'K{H}', f'Q{H}']
        community_cards_list: list[str] = [f'J{H}', f'T{H}', f'9{S}', f'2{S}', f'T{S}']
        player.set_all_cards(hole_cards, community_cards_list)
        self.assertTrue(player._all_cards.get(f'K{H}') == 13, 'Failed set_all_cards - test 1')
        self.assertTrue(player._all_cards.get(f'Q{H}') == 12, 'Failed set_all_cards - test 2')
        self.assertTrue(player._all_cards.get(f'J{H}') == 11, 'Failed set_all_cards - test 3')
        self.assertTrue(player._all_cards.get(f'T{H}') == 10, 'Failed set_all_cards - test 4')
        self.assertTrue(player._all_cards.get(f'9{S}') == 9, 'Failed set_all_cards - test 5')
        self.assertTrue(player._all_cards.get(f'2{S}') == 2, 'Failed set_all_cards - test 6')
        # Introduce an Ace
        hole_cards: list[str] = [f'A{H}', f'Q{H}']
        player.set_all_cards(hole_cards, community_cards_list)
        self.assertTrue(player._all_cards.get(f'A{H}') == 14, 'Failed set_all_cards - test 7')

    def test_set_player_ranking(self):
        player = Player(player_name='Player 1')
        player_name = 'Player 1'
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'Q{S}', f'4{C}', f'3{S}', f'2{S}']
        hand_cards = hole_cards + community_cards

        # Set all_cards to {'9♥': 9, 'K♥': 13, '9♦': 9, 'Q♠': 12, '4♣': 4, '3♠': 3, '2♠': 2}
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        player.find_highest_ranked_hand(card_list=community_cards, pocket_cards=hole_cards)
        # Set player ranking to: {'Player 1': [ ['One Pair', 15, 9], [13, 9] ]}
        player.set_player_ranking(hand_cards=hand_cards)

        # Test True
        self.assertTrue(player._player_ranking.get(player_name) == [['One Pair', 15, 9], [13, 9]],
                        'Failed set_player_ranking - Test 1')

    def test_get_cards_from_values(self):
        player = Player(player_name='Player 1')

        # Test ListEqual
        player.set_all_cards([f'A{H}', f'K{H}'], [f'Q{S}', f'J{H}', f'T{H}', f'9{H}', f'8{S}'])
        values = [14, 13, 12, 11, 10]
        cards = [f'A{H}', f'K{H}', f'Q{S}', f'J{H}', f'T{H}']
        self.assertListEqual(player.get_cards_from_values(values), cards, 'Failed get_cards_from_values - test 1')

        # Test ListEqual
        values = [14, 10]
        cards = [f'A{H}', f'T{H}']
        self.assertListEqual(player.get_cards_from_values(values), cards, 'Failed get_cards_from_values - test 2')

        # Test ListEqual
        values = [8, 9, 13]
        cards = [f'8{S}', f'9{H}', f'K{H}']
        self.assertListEqual(player.get_cards_from_values(values), cards, 'Failed get_cards_from_values - test 3')

    def test_set_player_name(self):
        player_name = 'Player 1'
        player1 = Player(player_name=player_name)
        # Test True
        self.assertTrue(player1.player_name == player_name,
                        'Failed test_set_player_name - Test 1')

    def test_set_ace_high(self):
        player_name = 'Player 1'
        player1 = Player(player_name=player_name)
        # Test True
        player1.set_best_hand_name('Flush')
        self.assertTrue(player1.ace_high,
                        'Failed test_set_ace_high - Test 1')
        player1.set_best_hand_name('Straight')
        self.assertFalse(player1.ace_high,
                         'Failed test_set_ace_high - Test 2')

    def test_set_player_score(self):
        player_name = 'Player 1'
        player1 = Player(player_name=player_name)
        player1.set_player_score(100)
        # Test True
        self.assertTrue(isinstance(player1._player_score, int),
                        'Failed test_set_player_score - Test 1')
        self.assertTrue(player1._player_score == 100,
                        'Failed test_set_player_score - Test 2')

    def test_get_Kicker(self):
        player = Player(player_name='Player 1')

        # Test False: King and Ace in hand
        hole_cards = [f'K{H}', f'A{H}']
        self.assertTrue(player.get_Kicker(hole_cards)[0] == 'Ace', "Failed Kicker - test 1")

        # Test True: best_hand set to Ace
        hole_cards = [f'A{H}', f'K{H}']
        self.assertTrue(player.get_Kicker(hole_cards)[0] == 'Ace', "Failed Kicker - test 2")

        # Test True: best_hand set to 3
        hole_cards = [f'3{H}', f'2{H}']
        self.assertTrue(player.get_Kicker(hole_cards)[0] == 'Three', "Failed Kicker - test 3")

        # Test True: best_hand set to T
        hole_cards = [f'9{H}', f'T{H}']
        self.assertTrue(player.get_Kicker(hole_cards)[0] == 'Ten', "Failed Kicker - test 4")

    def test_get_best_hand_cards(self):
        player = Player(player_name='Player 1')

        # Test ListEqual: Royal Flush returned and not the lower suited
        hand = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}']
        kicker = f'A{S}'
        player.set_best_hand_and_kicker(hand, kicker)
        self.assertListEqual(player.get_best_hand_cards(), [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}'],
                             "Failed test_get_best_hand_cards - test 1")

    def test_get_hole_cards(self):
        player = Player(player_name='Player 1')
        player.set_pocket_card(f'A{H}')
        player.set_pocket_card(f'K{H}')
        self.assertTrue(Counter(player.get_pocket_cards()) == Counter([f'A{H}', f'K{H}']),
                        "Failed get_hole_cards - test 1")

    def test_get_all_cards(self):
        player = Player(player_name='Player 1')
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'Q{S}', f'4{C}', f'3{S}', f'2{S}']
        all_cards = {'9♥': 9, 'K♥': 13, '9♦': 9, 'Q♠': 12, '4♣': 4, '3♠': 3, '2♠': 2}
        player.set_all_cards(hole_cards, community_cards)
        self.assertTrue(player.get_all_cards() == all_cards, "Failed get_all_cards - test 1")

    def test_get_best_hand_name(self):
        player = Player(player_name='Player 1')
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'Q{S}', f'4{C}', f'3{S}', f'2{S}']
        hand_cards = hole_cards + community_cards

        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        player.find_highest_ranked_hand(card_list=community_cards, pocket_cards=hole_cards)
        player.set_player_ranking(hand_cards=hand_cards)
        self.assertTrue(player.get_best_hand_name() == "One Pair", "Failed get_best_hand_name - test 1")

    def test_get_player_ranking(self):
        player = Player(player_name='Player 1')
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'Q{S}', f'4{C}', f'3{S}', f'2{S}']
        hand_cards = hole_cards + community_cards

        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        player.find_highest_ranked_hand(card_list=community_cards, pocket_cards=hole_cards)
        player.set_player_ranking(hand_cards=hand_cards)
        self.assertTrue(player.get_player_ranking() == {'Player 1': [['One Pair', 15, 9], [13, 9]]},
                        "Failed get_player_ranking - test 1")

    def test_get_player_score(self):
        player = Player(player_name='Player 1')
        player.set_player_score(100)
        self.assertTrue(player.get_player_score() == 100, "Failed get_player_score - test 1")

    def test_find_highest_ranked_hand(self):
        player = Player(player_name='Player 1')

        # Test True: Royal flush in hand
        cards_list = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'Royal Flush',
                        "Failed determine_highest_hand - test 1")

        # Test True: Straight flush in hand
        cards_list = [f'5{H}', f'4{H}', f'6{H}', f'7{H}', f'8{H}', f'9{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'Straight Flush',
                        "Failed determine_highest_hand - test 2")

        # Test True: Four of a kind in hand
        cards_list = [f'A{H}', f'A{D}', f'A{S}', f'A{C}', f'T{H}', f'9{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'Four of a Kind',
                        "Failed determine_highest_hand - test 3")

        # Test True: full house in hand
        cards_list = [f'A{H}', f'A{D}', f'A{S}', f'T{D}', f'T{H}', f'9{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'Full House',
                        "Failed determine_highest_hand - test 4")

        # Test True: flush in hand
        cards_list = [f'A{H}', f'9{H}', f'2{H}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'Flush',
                        "Failed determine_highest_hand - test 5")

        # Test True: Straight in hand
        cards_list = [f'3{D}', f'4{C}', f'5{H}', f'6{H}', f'7{H}', f'8{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'Straight',
                        "Failed determine_highest_hand - test 6")

        # Test True: Three of a kind in hand
        cards_list = [f'A{H}', f'A{D}', f'A{S}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'Three of a Kind',
                        "Failed determine_highest_hand - test 7")

        # Test True: Two Pair in hand
        cards_list = [f'A{H}', f'A{D}', f'J{S}', f'J{H}', f'T{H}', f'9{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'Two Pair',
                        "Failed determine_highest_hand - test 8")

        # Test True: Three of a kind in hand
        cards_list = [f'A{H}', f'A{D}', f'4{S}', f'J{H}', f'7{H}', f'9{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'One Pair',
                        "Failed determine_highest_hand - test 9")

        # Test False: No match - High Card result
        cards_list = [f'Q{H}', f'A{D}', f'J{S}', f'9{H}', f'7{H}', f'5{S}', f'2{S}']
        player.find_highest_ranked_hand(cards_list)
        self.assertTrue(player._best_hand_name == 'High Card',
                        "Failed determine_highest_hand - test 10")

    def test_find_royal_flush(self):
        player = Player(player_name='Player 1')
        # Test ListEqual: Royal Flush returned and not the lower suited
        hole_cards = [f'A{H}', f'K{H}']
        community_cards = [f'Q{H}', f'J{H}', f'T{H}', f'9{H}', f'2{S}']
        high_hand_list = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertListEqual(player.find_royal_flush(), high_hand_list, 'Failed find_royal_flush - Test 1')

        # Test ListEqual: Royal Flush returned and not the lower suited (hole cards with lower cards)
        hole_cards = [f'Q{H}', f'9{H}']
        community_cards = [f'A{H}', f'J{H}', f'T{H}', f'K{H}', f'2{S}']
        high_hand_list = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertListEqual(player.find_royal_flush(), high_hand_list, 'Failed find_royal_flush - Test 1')

    def test_find_highest_straight_flush(self):
        player = Player(player_name='Player 1')
        # Test ListEqual: Straight flush returned
        hole_cards = [f'2{S}', f'K{H}']
        community_cards = [f'Q{H}', f'J{H}', f'T{H}', f'9{H}', f'3{S}']
        high_hand_list = [f'9{H}', f'T{H}', f'J{H}', f'Q{H}', f'K{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertListEqual(player.find_highest_straight_flush(), high_hand_list,
                             'Failed find_highest_straight_flush - Test 1')

        # Test ListEqual: Straight flush returned
        hole_cards = [f'7{H}', f'K{H}']
        community_cards = [f'Q{H}', f'J{H}', f'T{H}', f'9{H}', f'8{H}']
        high_hand_list = [f'9{H}', f'T{H}', f'J{H}', f'Q{H}', f'K{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertListEqual(player.find_highest_straight_flush(), high_hand_list,
                             'Failed find_highest_straight_flush - Test 2')

    def test_find_four_of_a_kind(self):
        player = Player(player_name='Player 1')
        # Test True
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'9{S}', f'9{C}', f'3{S}', f'2{S}']
        high_hand_list = [f'9{H}', f'9{D}', f'9{S}', f'9{C}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_four_of_a_kind(), high_hand_list),
                        'Failed find_four_of_a_kind - Test 1')
        # Test True
        hole_cards = [f'2{S}', f'K{H}']
        community_cards = [f'9{D}', f'9{S}', f'9{C}', f'3{S}', f'9{H}']
        high_hand_list = [f'9{H}', f'9{D}', f'9{S}', f'9{C}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_four_of_a_kind(), high_hand_list),
                        'Failed find_four_of_a_kind - Test 2')

    def test_find_highest_boat(self):
        player = Player(player_name='Player 1')
        # Test True
        hole_cards = [f'9{H}', f'9{C}']
        community_cards = [f'9{D}', f'A{S}', f'A{C}', f'3{S}', f'2{S}']
        high_hand_list = [f'9{H}', f'9{C}', f'9{D}', f'A{S}', f'A{C}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_boat(), high_hand_list),
                        'Failed find_highest_boat - Test 1')
        # Test True
        hole_cards = [f'9{H}', f'9{C}']
        community_cards = [f'9{D}', f'A{S}', f'A{C}', f'A{H}', f'2{S}']
        high_hand_list = [f'9{H}', f'9{C}', f'A{S}', f'A{C}', f'A{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_boat(), high_hand_list),
                        'Failed find_highest_boat - Test 2')

    def test_find_highest_flush(self):
        player = Player(player_name='Player 1')
        # Test True
        hole_cards = [f'9{H}', f'T{H}']
        community_cards = [f'2{H}', f'4{H}', f'A{H}', f'3{S}', f'2{S}']
        high_hand_list = [f'9{H}', f'T{H}', f'2{H}', f'4{H}', f'A{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_flush(), high_hand_list),
                        'Failed find_highest_flush - Test 1')
        # Test True
        hole_cards = [f'9{H}', f'T{H}']
        community_cards = [f'K{H}', f'4{H}', f'A{H}', f'3{H}', f'2{H}']
        high_hand_list = [f'A{H}', f'K{H}', f'T{H}', f'9{H}', f'4{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_flush(), high_hand_list),
                        'Failed find_highest_flush - Test 2')

    def test_find_highest_straight(self):
        player = Player(player_name='Player 1')
        # Test ListEqual: Straight flush returned
        hole_cards = [f'2{S}', f'K{H}']
        community_cards = [f'Q{H}', f'J{H}', f'T{H}', f'9{H}', f'3{S}']
        high_hand_list = [f'9{H}', f'T{H}', f'J{H}', f'Q{H}', f'K{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)

        # Test ListEqual: Royal Flush returned and not the lower suited
        self.assertListEqual(player.find_highest_straight(), high_hand_list,
                             'Failed find_highest_straight - test 1')

        # Test ListEqual: High straight returned, not the lower straight
        hole_cards = [f'2{H}', f'3{D}']
        cards_list = [f'5{S}', f'4{C}', f'7{H}', f'6{D}', f'8{S}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=cards_list)
        self.assertListEqual(player.find_highest_straight(), [f'4{C}', f'5{S}', f'6{D}', f'7{H}', f'8{S}'],
                             'Failed find_highest_straight - test 2')

        # Test ListEqual: High straight returned (2-6), not the lower straight (A-5)
        hole_cards = [f'2{H}', f'3{D}']
        cards_list = [f'5{S}', f'4{C}', f'J{H}', f'6{D}', f'A{S}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=cards_list)
        self.assertListEqual(player.find_highest_straight(), [f'2{H}', f'3{D}', f'4{C}', f'5{S}', f'6{D}'],
                             'Failed find_highest_straight - test 3')

    def test_find_highest_three_of_a_kind(self):
        player = Player(player_name='Player 1')
        # Test True
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'9{S}', f'4{C}', f'3{S}', f'2{S}']
        high_hand_list = [f'9{H}', f'9{D}', f'9{S}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_three_of_a_kind(), high_hand_list),
                        'Failed find_highest_three_of_a_kind - Test 1')
        # Test True
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'9{S}', f'A{C}', f'A{S}', f'A{H}']
        high_hand_list = [f'A{C}', f'A{S}', f'A{H}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_three_of_a_kind(), high_hand_list),
                        'Failed find_highest_three_of_a_kind - Test 2')

    def test_find_highest_two_pair(self):
        player = Player(player_name='Player 1')
        # Test True
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'K{S}', f'4{C}', f'3{S}', f'2{S}']
        high_hand_list = [f'9{H}', f'9{D}', f'K{H}', f'K{S}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_two_pair(), high_hand_list),
                        'Failed find_highest_two_pair - Test 1')

        # Test True
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'K{S}', f'A{C}', f'A{S}', f'2{S}']
        high_hand_list = [f'K{H}', f'K{S}', f'A{C}', f'A{S}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_two_pair(), high_hand_list),
                        'Failed find_highest_two_pair - Test 2')

    def test_find_highest_pair(self):
        player = Player(player_name='Player 1')
        # Test True
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'Q{S}', f'4{C}', f'3{S}', f'2{S}']
        high_hand_list = [f'9{H}', f'9{D}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_pair(), high_hand_list),
                        'Failed find_highest_pair - Test 1')
        # Test True
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'8{D}', f'8{S}', f'4{C}', f'3{S}', f'2{S}']
        high_hand_list = [f'8{D}', f'8{S}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(player.all_cards_in_list(player.find_highest_pair(), high_hand_list),
                        'Failed find_highest_pair - Test 2')

    def test_find_high_cards(self):
        player = Player(player_name='Player 1')

        # Test True
        hole_cards = [f'9{H}', f'K{H}']
        community_cards = [f'9{D}', f'K{S}', f'4{C}', f'3{S}', f'2{S}']
        player.set_all_cards(pocket_cards=hole_cards, community_cards=community_cards)
        self.assertTrue(Counter(player.find_high_cards()) == Counter([f'K{H}', f'K{S}', f'9{H}', f'9{D}', f'4{C}']),
                        'Failed find_high_cards - Test 1')

        # Test False
        self.assertFalse(Counter(player.find_high_cards()) == Counter([f'K{H}', f'K{S}', f'9{H}', f'9{D}', f'3{S}']),
                         'Failed find_high_cards - Test 2')

    def test_tally_card_score(self):
        player = Player(player_name='Player 1')

        hand_1 = [f'2{D}', f'3{S}', f'4{C}', f'5{S}', f'6{D}']
        hand_2 = [f'3{S}', f'4{C}', f'5{S}', f'6{D}', f'7{S}']
        hand_3 = [f'7{S}', f'8{C}', f'9{S}', f'K{S}', f'A{S}']
        hand_4 = [f'T{S}', f'J{S}', f'Q{C}', f'K{S}', f'A{S}']
        hand_5 = [f'A{S}', f'2{D}', f'3{S}', f'4{C}', f'5{S}']

        # Test True
        self.assertTrue(player.tally_cards_score(hand_1) == 20,
                        "Failed tally_cards_score, test 1")
        self.assertTrue(player.tally_cards_score(hand_2) == 25,
                        "Failed tally_cards_score, test 2")
        player.set_best_hand_name('High_Card')
        self.assertTrue(player.tally_cards_score(hand_3) == 51,
                        "Failed tally_cards_score, test 3")
        self.assertTrue(player.tally_cards_score(hand_4) == 60,
                        "Failed tally_cards_score, test 4")
        player.set_best_hand_name('Straight')
        self.assertTrue(player.tally_cards_score(hand_5) == 15,
                        "Failed tally_cards_score, test 5")

    def test_score_the_hand(self):
        player = Player(player_name='Player 1')
        player.set_best_hand_name('Royal_Flush')

        # Test True
        cards_list = [f'A{H}', f'K{H}', f'Q{H}', f'J{H}', f'T{H}']
        self.assertTrue(player.score_the_hand(cards_list) == 10060,
                        "Failed score_the_hand - test 1")

        # Test True
        cards_list = [f'A{H}', f'2{H}', f'3{H}', f'4{H}', f'5{S}']
        player.set_best_hand_name('Straight')
        self.assertTrue(player.score_the_hand(cards_list) == 5015,
                        "Failed score_the_hand - test 2")

    # Test bookie class
    def test_get_winning_percentage(self):
        bookmaker = Bookie()

        # Test True: K -> A will yield 66
        win_tup = [f'K', f'A']
        self.assertTrue(bookmaker.get_winning_percentage(win_tup) == 66, 'Failed get_winning_percentage - test 1')

        # Test True: A -> K will yield 68
        win_tup = [f'A', f'K']
        self.assertTrue(bookmaker.get_winning_percentage(win_tup) == 68, 'Failed get_winning_percentage - test 2')

        # Test True: 2 -> A will yield 57
        win_tup = [f'2', f'A']
        self.assertTrue(bookmaker.get_winning_percentage(win_tup) == 57, 'Failed get_winning_percentage - test 3')

        # Test True: A -> 2 will yield 59
        win_tup = [f'A', f'2']
        self.assertTrue(bookmaker.get_winning_percentage(win_tup) == 59, 'Failed get_winning_percentage - test 4')

        # Test True: 2 -> 2 will yield 51
        win_tup = [f'2', f'2']
        self.assertTrue(bookmaker.get_winning_percentage(win_tup) == 51, 'Failed get_winning_percentage - test 5')

        # Test True: A -> A will yield 85
        win_tup = [f'A', f'A']
        self.assertTrue(bookmaker.get_winning_percentage(win_tup) == 85, 'Failed get_winning_percentage - test 6')

    # Test the Adjudicator class
    def test_comparitor(self):
        player1 = Player(player_name="Alice")
        player1.set_player_score(80)
        player2 = Player(player_name="Bob")
        player2.set_player_score(65)
        player3 = Player(player_name="Charlie")
        player3.set_player_score(50)

        rankings = Adjudicator.comparitor([player1, player2, player3])

        self.assertTrue(rankings.get(1) == "Alice",
                        "Failed test_comparitor - test 1")
        self.assertTrue(rankings.get(2) == "Bob",
                        "Failed test_comparitor - test 2")
        self.assertTrue(rankings.get(3) == "Charlie",
                        "Failed test_comparitor - test 3")

    # Test Game Manager
    def test_make_players(self):
        # Test make_players
        # Test get_player
        new_game = GameManager()
        players = {'Alice', 'Bob', 'Charlie'}
        new_game.make_players(players)
        new_game.get_player('Alice').set_player_score(50)
        new_game.get_player('Bob').set_player_score(80)
        new_game.get_player('Charlie').set_player_score(65)

        # Test True
        self.assertTrue(new_game.get_player('Alice').get_player_score() == 50,
                        "Failed test_make_players - test 1")
        self.assertTrue(new_game.get_player('Bob').get_player_score() == 80,
                        "Failed test_make_players - test 2")
        self.assertTrue(new_game.get_player('Charlie').get_player_score() == 65,
                        "Failed test_make_players - test 3")

    def test_get_all_players(self):
        new_game = GameManager()
        players = {'Alice', 'Bob', 'Charlie'}
        new_game.make_players(players)

        list_of_players = [new_game.get_player('Alice'),
                           new_game.get_player('Bob'),
                           new_game.get_player('Charlie')]

        # Test True
        self.assertTrue(Counter(new_game.get_all_players()) == Counter(list_of_players),
                        "Failed test_get_all_players - test 1")


# Run tests:
if __name__ == '__main__':
    unittest.main()
