from dealer import *
from game_manager import *
from bookie import *
from adjudicator import *


game = GameManager()
players = {'Alice', 'Bob', 'Charlie'}
game.make_players(players)
game.get_all_players()

deal = Dealer()
game_cards = deal.shuffle_deck()

deal.deal_out_cards_and_flop(players, game)
deal.deal_out_a_single_card()
deal.deal_out_a_single_card()
print(deal.get_community_cards())
for player in players:
    player_name = game.get_player(player).get_player_name()
    pocket_cards = game.get_player(player).get_pocket_cards()
    print(f'Player: {player_name}, Pocket Cards: {pocket_cards}')

for player in players:
    cc = deal.get_community_cards()
    pc = game.get_player(player).get_pocket_cards()
    game.get_player(player).find_highest_ranked_hand(card_list=cc, pocket_cards=pc)
    print(game.get_player(player).get_best_hand_name())

# I need to find the best 5 cards and add them to the player hand list.
