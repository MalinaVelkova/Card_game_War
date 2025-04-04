from War_Game_Cards.player import Player


class AIPlayer(Player):
    def __init__(self, name, deck):
        super().__init__(name, deck)

    def auto_draw(self):
        return self.deck.draw_card()
