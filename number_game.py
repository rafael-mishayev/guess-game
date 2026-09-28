import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7


def play_number_game():
    """Play one round of the number guessing game. Returns True on win."""
    target = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"\nGuess a number between {MIN_NUMBER} and {MAX_NUMBER}. "
          f"You have {MAX_ATTEMPTS} attempts.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = _read_guess(attempt)
        if guess is None:
            continue

        if guess == target:
            print(f"Correct! The number was {target}. "
                  f"You got it in {attempt} attempt(s).")
            return True
        elif guess < target:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of attempts. The number was {target}.")
    return False


def _read_guess(attempt):
    raw = input(f"Attempt {attempt}: ")
    try:
        value = int(raw)
    except ValueError:
        print("Please enter a whole number.")
        return None

    if not (MIN_NUMBER <= value <= MAX_NUMBER):
        print(f"Enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
        return None

    return value
