import random

WORDS = [
    "python", "keyboard", "developer", "elephant", "mountain",
    "guitar", "sandwich", "umbrella", "volcano", "printer",
]
MAX_WRONG_GUESSES = 6


def play_word_game():
    """Play one round of hangman-style word guessing. Returns True on win."""
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print(f"\nGuess the hidden word. You may miss up to "
          f"{MAX_WRONG_GUESSES} times.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(f"\nWord: {_render(word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        letter = _read_letter(guessed_letters)
        if letter is None:
            continue
        guessed_letters.add(letter)

        if letter not in word:
            wrong_guesses += 1
            print("Not in the word.")
        elif all(ch in guessed_letters for ch in word):
            print(f"\nCorrect! The word was '{word}'.")
            return True

    print(f"\nOut of guesses. The word was '{word}'.")
    return False


def _render(word, guessed_letters):
    return " ".join(ch if ch in guessed_letters else "_" for ch in word)


def _read_letter(guessed_letters):
    raw = input("Guess a letter: ").strip().lower()
    if len(raw) != 1 or not raw.isalpha():
        print("Please enter a single letter.")
        return None
    if raw in guessed_letters:
        print("You already guessed that letter.")
        return None
    return raw
