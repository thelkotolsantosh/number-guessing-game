"""
Number Guessing Game
====================
A simple command-line game where the player tries to guess a randomly
generated number within a given range. The game tracks the number of
attempts and gives hints after each guess.
"""

import random


def get_random_number(low: int = 1, high: int = 100) -> int:
    """
    Generate a random integer between low and high (inclusive).

    Args:
        low (int): The lower bound of the range. Default is 1.
        high (int): The upper bound of the range. Default is 100.

    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(low, high)


def get_hint(guess: int, secret: int) -> str:
    """
    Return a hint string based on how the guess compares to the secret number.

    Args:
        guess (int): The player's guess.
        secret (int): The secret number to be guessed.

    Returns:
        str: A hint — 'Too high!', 'Too low!', or 'Correct!'.
    """
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"


def get_player_guess(low: int, high: int) -> int:
    """
    Prompt the player for a valid integer guess within the given range.
    Keeps asking until a valid input is provided.

    Args:
        low (int): The lower bound of the allowed range.
        high (int): The upper bound of the allowed range.

    Returns:
        int: A valid integer guess from the player.
    """
    while True:
        try:
            guess = int(input(f"Enter your guess ({low}-{high}): "))
            if low <= guess <= high:
                return guess
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_game(low: int = 1, high: int = 100) -> int:
    """
    Run a single round of the Number Guessing Game.

    The player is asked to guess a randomly generated number within the range.
    After each guess, a hint is provided. The game ends when the player
    guesses correctly.

    Args:
        low (int): Lower bound of the guessing range. Default is 1.
        high (int): Upper bound of the guessing range. Default is 100.

    Returns:
        int: The number of attempts it took the player to guess correctly.
    """
    print(f"\n🎯 I'm thinking of a number between {low} and {high}.")
    print("Can you guess what it is?\n")

    secret = get_random_number(low, high)
    attempts = 0

    while True:
        guess = get_player_guess(low, high)
        attempts += 1
        hint = get_hint(guess, secret)
        print(f"  → {hint}")

        if hint == "Correct!":
            print(f"\n🎉 You got it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            break

    return attempts


def main():
    """
    Entry point for the Number Guessing Game.
    Displays a welcome message and allows the player to play multiple rounds.
    """
    print("=" * 40)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 40)

    while True:
        play_game()

        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
