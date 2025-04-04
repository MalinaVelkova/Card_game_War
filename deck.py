import random

from War_Game_Cards.card import Card


class Deck:
    def __init__(self, cards: list = None):
        self.cards = cards if cards else [Card(rank, suit) for suit in Card.SUITS for rank in Card.VALUES]

    # def __init__(self):
    # self.cards = [Cards(rank, suit) for suit in Cards.SUITS for rank in Cards.VALUES]
    # self.cards = cards if cards is not None else [
    #     Cards(rank, suit) for suit in Cards.SUITS for rank in Cards.VALUES
    # ]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0) if self.cards else None

    def draw_three_cards(self):
        num_to_draw = min(3, len(self.cards))
        return [self.draw_card() for _ in range(num_to_draw)]
        # if len(self.cards) >= 3:
        #     return [self.draw_card() for _ in range(3)]
        # else:
        #     return None

    def deal_cards(self):
        half = len(self.cards) // 2
        first_half = self.cards[:half]
        second_half = self.cards[half:]
        return first_half, second_half

    def is_empty(self):
        # return self.player_1.deck.is_empty() or self.player_2.deck.is_empty()
        return len(self.cards) == 0

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])


