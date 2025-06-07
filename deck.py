import random

from card import Card


class Deck:
    def __init__(self, cards: list = None):
        self.cards = cards if cards else [Card(rank, suit) for suit in Card.SUITS for rank in Card.VALUES]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0) if self.cards else None

    def draw_three_cards(self):
        num_to_draw = min(3, len(self.cards))
        return [self.draw_card() for _ in range(num_to_draw)]

    def deal_cards(self):
        half = len(self.cards) // 2
        first_half = self.cards[:half]
        second_half = self.cards[half:]
        return first_half, second_half

    def is_empty(self):
        return len(self.cards) == 0

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])
