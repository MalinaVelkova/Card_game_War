from game_logic import GameLogic
from war import War


class Game(GameLogic):
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.war_logic = War(player_1, player_2)
        self.turn = 1  # 1 for player_1, 2 for player_2
        self.first_card = None
        self.second_card = None

    def compare_cards(self):
        if self.player_1.deck.is_empty() or self.player_2.deck.is_empty():
            return self.declare_winner()

        if self.turn == 1:
            self.first_card = self.player_1.deck.draw_card()
            self.turn = 2
            return f"{self.player_1.name} draws {self.first_card}"
        else:
            self.second_card = self.player_2.deck.draw_card()
            self.turn = 1
            result = f"{self.player_2.name} draws {self.second_card}\n"

            if self.first_card and self.second_card:
                if self.first_card.value > self.second_card.value:
                    self.player_1.deck.cards.extend([self.first_card, self.second_card])
                    result += f"{self.player_1.name} takes"
                elif self.first_card.value < self.second_card.value:
                    self.player_2.deck.cards.extend([self.second_card, self.first_card])
                    result += f"{self.player_2.name} takes"
                else:
                    result += "WAR!\n"
                    print(result)
                    return self.war_logic.war()

            self.first_card = None
            self.second_card = None
            return result

    def declare_winner(self):
        if self.player_1.deck.is_empty():
            return (f"Game over!\n{self.player_1.name} is out of cards\n"
                    f"Congratulations! {self.player_2.name} wins!")
        if self.player_2.deck.is_empty():
            return (f"Game over!\n{self.player_2.name} is out of cards\n"
                    f"Congratulations! {self.player_1.name} wins!")
        return None

    def play_game(self):
        while True:
            result = self.compare_cards()
            print(result, "\n")
            if result.startswith("Game over!"):
                break
