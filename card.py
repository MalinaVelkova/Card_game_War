class Card:
    SUITS = ['♥', '♦', '♣', '♠']
    VALUES = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.VALUES[rank]

    def __str__(self):
        return f"{self.rank} {self.suit}"
