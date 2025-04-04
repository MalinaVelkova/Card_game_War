import time

import keyboard

from War_Game_Cards.ai_player import AIPlayer
from War_Game_Cards.deck import Deck
from War_Game_Cards.game import Game
from War_Game_Cards.player import Player


def main():
    print("Welcome to the War Game!")
    deck = Deck()
    deck.shuffle()

    first_half, second_half = deck.deal_cards()
    player1 = Player(input('Enter a name for player 1: '), Deck(first_half))

    while True:
        choice = input(
            "Do you want to play against an AI or another player? (Enter 'AI' or 'player'): ").strip().lower()
        if choice == 'ai':
            player2 = AIPlayer("AI Player", Deck(second_half))
            break
        elif choice == 'player':
            player2 = Player(input('Enter a name for player 2: '), Deck(second_half))
            break
        else:
            print("Invalid choice. Please enter 'AI' or 'player'.")

    if isinstance(player2, AIPlayer):
        print(f"\nPress 'Enter' for Player {player1.get_name()} to draw a card")
        print(f"AI Player ({player2.get_name()}) will auto-draw a card")
    else:
        print(f"\nPress 'A' for Player {player1.get_name()} to draw a card")
        print(f"Press 'L' for Player {player2.get_name()} to draw a card")
    print("Press 'Q' to quit\n")

    print(f"{player1.get_name()}'s deck: {player1.get_deck()}")
    print(f"{player2.get_name()}'s deck: {player2.get_deck()}\n")
    game = Game(player1, player2)

    while True:
        if keyboard.is_pressed("q"):
            print("Quitting game...")
            break
        elif keyboard.is_pressed("enter") and game.turn == 1 and isinstance(player2, AIPlayer):
            result = game.compare_cards()
            print(result)
            if result.startswith("Game over!"):
                break
            time.sleep(0.5)
        elif keyboard.is_pressed("a") and game.turn == 1 and isinstance(player2, Player):
            result = game.compare_cards()
            print(result)
            if result.startswith("Game over!"):
                break
            time.sleep(0.5)
        elif keyboard.is_pressed("l") and game.turn == 2 and isinstance(player2, Player):
            result = game.compare_cards()
            print(result)
            if result.startswith("Game over!"):
                break
            time.sleep(0.5)
        elif isinstance(player2, AIPlayer) and game.turn == 2:
            result = game.compare_cards()
            print(result)
            if result.startswith("Game over!"):
                break
            time.sleep(0.5)


if __name__ == "__main__":
    main()
