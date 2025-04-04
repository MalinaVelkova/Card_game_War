from War_Game_Cards.game_logic import GameLogic
from War_Game_Cards.war import War


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
            # return self.war_logic.war()

            # return result

    # def war(self):
    #     if self.player_1.deck.is_empty() or self.player_2.deck.is_empty():
    #         return self.declare_winner()
    #
    #     war_pile_1 = []
    #     war_pile_2 = []
    #
    #     for _ in range(3):
    #         if self.player_1.deck.is_empty() or self.player_2.deck.is_empty():
    #             return self.declare_winner()
    #         war_pile_1.append(self.player_1.deck.draw_card())
    #         war_pile_2.append(self.player_2.deck.draw_card())
    #
    #     result = ""
    #     for i in range(3):
    #         result += f"{self.player_1.name} draws {war_pile_1[i]}\n"
    #         result += f"{self.player_2.name} draws {war_pile_2[i]}\n"
    #
    #     third_card = war_pile_1[2]
    #     sixth_card = war_pile_2[2]
    #
    #     if third_card.value > sixth_card.value:
    #         self.player_1.deck.cards.extend(war_pile_1 + war_pile_2)
    #         result += f"{self.player_1.name} wins the war"
    #     elif third_card.value < sixth_card.value:
    #         self.player_2.deck.cards.extend(war_pile_2 + war_pile_1)
    #         result += f"{self.player_2.name} wins the war"
    #     else:
    #         result += "Another WAR!\n"
    #         self.war_counter = 6  # Another 3 cards from each player
    #     return result

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

            # if self.war_mode:
            #     result = self.war()
            # else:
            #     result = self.compare_cards()
            # print(result, "\n")
            # if result.startswith("Game over!"):
            #     break

# class Game(GameLogic):
#     def __init__(self, player_1, player_2):
#         self.player_1 = player_1
#         self.player_2 = player_2
#         self.war_logic = War(player_1, player_2)
#         self.turn = 1  # 1 for player_1, 2 for player_2
#         self.war_mode = False
#         self.war_counter = 0  # Initialize war_counter
#         self.first_card = None
#         self.second_card = None
#
#     def compare_cards(self):
#         if self.is_any_deck_empty():
#             return self.declare_winner()
#
#         if self.turn == 1:
#             self.first_card = self.player_1.deck.draw_card()
#             self.turn = 2
#             return f"{self.player_1.name} draws {self.first_card}"
#         else:
#             self.second_card = self.player_2.deck.draw_card()
#             self.turn = 1
#             result = f"{self.player_2.name} draws {self.second_card}\n"
#
#             if self.first_card and self.second_card:
#                 if self.first_card.value > self.second_card.value:
#                     self.player_1.deck.cards.extend([self.first_card, self.second_card])
#                     result += f"{self.player_1.name} takes"
#                 elif self.first_card.value < self.second_card.value:
#                     self.player_2.deck.cards.extend([self.second_card, self.first_card])
#                     result += f"{self.player_2.name} takes"
#                 else:
#                     result += "WAR!\n"
#                     self.war_mode = True
#                     self.war_counter = 6
#                     result += self.war()
#
#             self.first_card = None
#             self.second_card = None
#             return result
#
#     def war(self):
#         if self.war_counter > 0:
#             self.war_counter -= 1
#             return "Waiting for WAR cards to be drawn"
#         else:
#             result = self.war_logic.war()
#             self.war_mode = False
#             return result
#
#     def is_any_deck_empty(self):
#         return self.player_1.deck.is_empty() or self.player_2.deck.is_empty()
#
#     def declare_winner(self):
#         if self.player_1.deck.is_empty():
#             return (f"Game over!\n{self.player_1.name} is out of cards\n"
#                     f"Congratulations! {self.player_2.name} wins!")
#         if self.player_2.deck.is_empty():
#             return (f"Game over!\n{self.player_2.name} is out of cards\n"
#                     f"Congratulations! {self.player_1.name} wins!")
#         return None
#
#     def play_game(self):
#         while True:
#             result = self.compare_cards()
#             print(result, "\n")
#             if result.startswith("Game over!"):
#                 break
