## A Texas Holdem Poker game generator. 
- To be used for statistical and strategy analysis.

## Class Structure

### Player
Extends Rankinator, tracks the player activity and card play.
Vars:
- Hole cards (player cards)
- Bankroll (player bank total)
- Highest hand name (high hand of the player)
- Highest hand cards
- Current bet
- Name

## Rankinator
Rankinator is a list of tools that are used to calculate the best hand that a player holds.
Vars:
- hole_cards : Cards held by player
- community_cards : The cards shared by all players
- all_cards : Individual to each player. hole cards and community cards
- all_cards_ranked : A list of the integer ranks of all cards.
- best_hand : The name of the best hand that the player holds
- best_hand_rank : Used to compare two hands by the Adjudicator class
- kicker_rank : The rank of the kicker card held by the player

## Dealer
Extends Rankinator, tracks the cards on the table (Burner cards, Flop, Turn, River)
Manages the game turn sequence, deck, D/B/DB position.

## Bookie
Calculates probability of hand winning. 
Calculates the best bet to put forward. 
Randomly generates noise as a given level. 
Calculates the likelihood of required cards for a win. 
Manages Pot and player bets.

## Adjudicator
Makes the judgement of whose hand is highest. 

## Table
manages the visual information output to the console.

## Run
Game manager. Runs the game and starts the next round etc. 

## Deck 
Not a class but a list of constants:
- Deck
- Card rank
- Shuffler
- Unicode characters for suits.
