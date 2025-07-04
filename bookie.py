class Bookie:

    def __init__(self):
        self.opening_winning_odds = [
            [85, 68, 67, 66, 66, 64, 63, 63, 62, 62, 61, 60, 59],  # A
            [66, 83, 64, 64, 63, 61, 60, 59, 58, 58, 57, 56, 55],  # K
            [65, 62, 80, 61, 61, 59, 58, 56, 55, 55, 54, 53, 52],  # Q
            [65, 62, 59, 78, 59, 57, 56, 54, 53, 52, 51, 50, 50],  # J
            [64, 61, 59, 57, 75, 56, 54, 53, 51, 49, 49, 48, 47],  # T
            [62, 59, 57, 55, 53, 72, 53, 51, 50, 48, 46, 46, 45],  # 9
            [61, 58, 55, 53, 52, 50, 69, 50, 49, 47, 45, 43, 43],  # 8
            [60, 57, 54, 52, 50, 48, 47, 67, 48, 46, 45, 43, 41],  # 7
            [59, 56, 53, 50, 48, 47, 46, 45, 64, 46, 44, 42, 40],  # 6
            [60, 55, 52, 49, 47, 45, 44, 43, 43, 61, 44, 43, 41],  # 5
            [59, 54, 51, 48, 46, 43, 42, 41, 41, 41, 58, 42, 40],  # 4
            [58, 54, 50, 48, 45, 43, 40, 39, 39, 39, 39, 55, 39],  # 3
            [57, 53, 49, 47, 44, 42, 40, 37, 37, 37, 36, 35, 51]   # 2
            # A   K   Q   J   T   9   8   7   6   5   4   3   2
        ]

        # Map card ranks to indices in the matrix
        self.card_index = {
            'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}

    # Function to get the winning percentage from a tuple of two cards
    def get_winning_percentage(self, card_tuple):
        # Accepts a tuple with the suits removed.
        card1, card2 = card_tuple

        # Get the indices from the card_index map
        index1 = self.card_index[card1]
        index2 = self.card_index[card2]

        # The matrix is symmetric, so we can always access the "upper triangle"
        return self.opening_winning_odds[index1][index2]
