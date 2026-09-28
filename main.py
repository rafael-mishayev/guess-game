from number_game import play_number_game
from word_game import play_word_game

MENU = """
=== Guess Game ===
1. Number guessing
2. Word guessing (hangman)
3. Show score
4. Quit
"""


def main():
    score = {"wins": 0, "losses": 0}

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            _record(score, play_number_game())
        elif choice == "2":
            _record(score, play_word_game())
        elif choice == "3":
            print(f"\nScore — wins: {score['wins']}, losses: {score['losses']}")
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option, please choose 1-4.")


def _record(score, won):
    score["wins" if won else "losses"] += 1


if __name__ == "__main__":
    main()
