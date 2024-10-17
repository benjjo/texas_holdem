import random

# Unicode characters for card suits
H = "\u2665"  # Hearts
D = "\u2666"  # Diamonds
C = "\u2663"  # Clubs
S = "\u2660"  # Spades

DECK = [
    f'2{S}',f'3{S}',f'4{S}',f'5{S}',f'6{S}',f'7{S}',f'8{S}',f'9{S}',f'10{S}',f'J{S}',f'Q{S}',f'K{S}',f'A{S}',
    f'2{C}',f'3{C}',f'4{C}',f'5{C}',f'6{C}',f'7{C}',f'8{C}',f'9{C}',f'10{C}',f'J{C}',f'Q{C}',f'K{C}',f'A{C}',
    f'2{D}',f'3{D}',f'4{D}',f'5{D}',f'6{D}',f'7{D}',f'8{D}',f'9{D}',f'10{D}',f'J{D}',f'Q{D}',f'K{D}',f'A{D}',
    f'2{H}',f'3{H}',f'4{H}',f'5{H}',f'6{H}',f'7{H}',f'8{H}',f'9{H}',f'10{H}',f'J{H}',f'Q{H}',f'K{H}',f'A{H}']


def shuffle_deck():
    burner_deck = DECK.copy()
    random.shuffle(burner_deck)
    return burner_deck


