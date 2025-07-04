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

## GameManager
Game manager. Runs the game and starts the next round etc. 

## Deck 
Constants associated with the deck and cards. 

## Language

Texas Hold’em Poker Terms & Definitions

| Term             | Definition |
|------------------|------------|
| **Pre-Flop**     | The stage after players receive their two hole cards but before any community cards are dealt. |
| **Flop**         | The first three community cards dealt face up. |
| **Turn**         | The fourth community card, also called "Fourth Street." |
| **River**        | The fifth and final community card, also called "Fifth Street." |
| **Showdown**     | When players reveal their hands to determine the winner after the final betting round. |
| **Check**        | Decline to bet, while keeping the option to call or raise later in the round. |
| **Bet**          | Place chips into the pot. |
| **Call**         | Match the current highest bet made by another player. |
| **Raise**        | Increase the current bet amount. |
| **Re-raise**     | Raise again after another player has already raised. |
| **Fold**         | Discard your hand and forfeit the pot. |
| **All-In**       | Bet all your remaining chips. |
| **Pot**          | The total chips wagered in the current hand. |
| **Pot Odds**     | Ratio of the pot size to the cost of a contemplated call. |
| **3-Bet**        | A re-raise, i.e. the third bet in a betting sequence. |
| **C-Bet**        | A continuation bet made on the flop by the pre-flop raiser. |
| **Value Bet**    | Bet made hoping to be called by worse hands. |
| **Bluff**        | Bet or raise with a weak hand to make opponents fold stronger hands. |
| **Semi-Bluff**   | Bet with a drawing hand that could become strong later. |
| **Check-Raise**  | Check, then raise after an opponent bets. |
| **Overbet**      | Betting more than the current pot size. |
| **Underbet**     | Betting much less than the pot. |
| **Outs**         | Cards that will improve your hand to likely win. |
| **Drawing Dead** | No remaining cards can improve your hand to win. |
| **Kicker**       | The next highest card outside your main hand, used to break ties. |
| **Nuts**         | The best possible hand at a given time. |
| **Set**          | Three of a kind using a pocket pair plus one community card. |
| **Trips**        | Three of a kind using one hole card and two community cards. |
| **Straight**     | Five sequential cards of any suits. |
| **Flush**        | Five cards of the same suit, not in sequence. |
| **Full House**   | Three of a kind plus a pair. |
| **Quads**        | Four of a kind. |
| **Straight Flush** | Five sequential cards of the same suit. |
| **Royal Flush**  | A♠ K♠ Q♠ J♠ 10♠ — the highest possible straight flush. |
| **Blinds**       | Forced bets (small blind & big blind) posted before cards are dealt. |
| **Button**       | Marks who is acting as dealer for the hand; moves clockwise. |
| **UTG**          | "Under the Gun" — the player immediately left of the big blind, acts first pre-flop. |
| **Cutoff**       | Seat right before the button, often used for stealing blinds. |
| **Hijack**       | Seat right before the cutoff. |
| **Heads-Up**     | A hand contested between only two players. |
| **Muck**         | To fold or discard your hand without showing it. |
| **Slow Roll**    | Taking unnecessary time to reveal a winning hand; considered poor etiquette. |
| **Snap Call**    | Instantly calling a bet, showing strong confidence. |
| **Tank**         | Taking a long time to think before acting. |
| **Straddle**     | An optional blind bet made before cards are dealt to "buy" last action pre-flop. |
