from player import Player


class  BotPlayer(Player):
    def __init__(self, name, deck):
        super().__init__(name, deck)

    def auto_draw(self):
        return self.deck.draw_card()
