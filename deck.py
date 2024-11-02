# Unicode characters for card suits
H = "\u2665"  # ♥ Hearts
D = "\u2666"  # ♦ Diamonds
C = "\u2663"  # ♣ Clubs
S = "\u2660"  # ♠ Spades

DECK = [
    f'2{S}',f'3{S}',f'4{S}',f'5{S}',f'6{S}',f'7{S}',f'8{S}',f'9{S}',f'T{S}',f'J{S}',f'Q{S}',f'K{S}',f'A{S}',
    f'2{C}',f'3{C}',f'4{C}',f'5{C}',f'6{C}',f'7{C}',f'8{C}',f'9{C}',f'T{C}',f'J{C}',f'Q{C}',f'K{C}',f'A{C}',
    f'2{D}',f'3{D}',f'4{D}',f'5{D}',f'6{D}',f'7{D}',f'8{D}',f'9{D}',f'T{D}',f'J{D}',f'Q{D}',f'K{D}',f'A{D}',
    f'2{H}',f'3{H}',f'4{H}',f'5{H}',f'6{H}',f'7{H}',f'8{H}',f'9{H}',f'T{H}',f'J{H}',f'Q{H}',f'K{H}',f'A{H}']

RANKS_MAP = {1:'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
             10:'Ten', 11:'Jack', 12:'Queen', 13:'King', 14:'Ace', 15:'One Pair', 16:'Two Pair',
             17:'Three of a Kind', 18:'Straight', 19:'Flush', 20:'Full House', 21:'Four of a Kind',
             22:'Straight Flush', 23:'Royal Flush'}

HANDS_MAP = {'Two': 2,'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
             'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14, 'One Pair': 15, 'Two Pair': 16,
             'Three of a Kind': 17, 'Straight': 18, 'Flush': 19, 'Full House': 20, 'Four of a Kind': 21,
             'Straight Flush': 22, 'Royal Flush': 23}

CARDS_MAP = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6':6, '5': 5, '4': 4, '3': 3, '2': 2}
