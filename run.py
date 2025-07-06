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
