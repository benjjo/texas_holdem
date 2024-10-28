## A Texas Holdem Poker game generator. 
- To be used for statistical and strategy analysis.

## Class Structure

### Player
Extends Rankinator, tracks the player activity and card play.
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

## Rankinator
Rankinator is a list of tools that are used to calculate the best hand that a player holds.

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
        self.best_hand_rank :  integer
            Used to compare two hands by the Adjudicator class
        self.kicker_rank :  integer
            The rank of the kicker card held by the player

## Dealer
Tracks the cards on the table (Burner cards, Flop, Turn, River)
Manages the game turn sequence, deck, D/B/DB position.
Manages Pot and player bets.

## Bookie
Calculates probability of hand winning. 
Calculates the best bet to put forward. 
Randomly generates noise as a given level. 
Calculates the likelihood of required cards for a win. 

## Adjudicator
Makes the judgement of whose hand is highest. 

## Table
manages the visual information output to the console.

## Run
Game manager. Runs the game and starts the next round etc. 

## Deck 
Constants associated with the deck and cards. 
