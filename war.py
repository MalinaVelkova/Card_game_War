from war_logic import WarLogic


class War(WarLogic):
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def war(self):
        war_pile_first = []
        war_pile_second = []
        while True:
            if self.player_1.deck.is_empty() or self.player_2.deck.is_empty():
                return self.print_empty_deck()

            first_set = self.player_1.deck.draw_three_cards()
            second_set = self.player_2.deck.draw_three_cards()

            if len(first_set) < 3:
                return (f"Game over!\n{self.player_1.name} doesn't have enough cards for war\n"
                        f"Congratulations! {self.player_2.name} wins!")
            if len(second_set) < 3:
                return (f"Game over!\n{self.player_2.name} doesn't have enough cards for war\n"
                        f"Congratulations! {self.player_1.name} wins!")

            war_pile_first.extend(first_set)
            war_pile_second.extend(second_set)

            third_card = first_set[-1]
            sixth_card = second_set[-1]

            print(f"{self.player_1.name} draws {third_card}")
            print(f"{self.player_2.name} draws {sixth_card}")

            if third_card.value > sixth_card.value:
                self.player_1.deck.cards.extend(war_pile_first + war_pile_second)
                return f"{self.player_1.name} wins the war"
            elif third_card.value < sixth_card.value:
                self.player_2.deck.cards.extend(war_pile_second + war_pile_first)
                return f"{self.player_2.name} wins the war"
            else:
                print("Another WAR!\n")
                return self.war()  # Call the war method again to handle the "Another WAR" case

    def is_any_deck_empty(self):
        return self.player_1.deck.is_empty() or self.player_2.deck.is_empty()

    def print_empty_deck(self):
        if self.player_1.deck.is_empty():
            return (f"Game over!\n{self.player_1.name} is out of cards\n"
                    f"Congratulations! {self.player_2.name} wins!")
        if self.player_2.deck.is_empty():
            return (f"Game over!\n{self.player_2.name} is out of cards\n"
                    f"Congratulations! {self.player_1.name} wins!")
        return None

