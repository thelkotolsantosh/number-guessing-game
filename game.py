"""
Number Guessing Game
====================
A simple command-line game where the player tries to guess a randomly
generated number within a given range. The game tracks the number of
attempts, saves scores, and gives hints after each guess.
"""

import random
import json
from datetime import datetime

SCORES_FILE = "scores.json"


def load_scores() -> dict:
    """
    Load scores from the JSON file.

    Returns:
        dict: Score data.
    """
    try:
        with open(SCORES_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"high_scores": []}


def save_scores(data: dict) -> None:
    """
    Save scores to the JSON file.

    Args:
        data (dict): Score data to save.
    """
    with open(SCORES_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_score(player_name: str, attempts: int) -> None:
    """
    Add a player's score to the leaderboard.

    Args:
        player_name (str): Name of the player.
        attempts (int): Number of attempts taken.
    """
    data = load_scores()

    score_entry = {
        "name": player_name,
        "attempts": attempts,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data["high_scores"].append(score_entry)

    # Sort by lowest attempts
    data["high_scores"] = sorted(
        data["high_scores"],
        key=lambda x: x["attempts"]
    )

    # Keep only top 10 scores
    data["high_scores"] = data["high_scores"][:10]

    save_scores(data)


def display_leaderboard() -> None:
    """
    Display the top scores leaderboard.
    """
    data = load_scores()

    print("\n🏆 LEADERBOARD")
    print("=" * 40)

    if not data["high_scores"]:
        print("No scores yet.")
        return

    for index, score in enumerate(data["high_scores"], start=1):
        print(
            f"{index}. "
            f"{score['name']} - "
            f"{score['attempts']} attempts "
            f"({score['date']})"
        )


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

    Args:
        low (int): Lower bound of the guessing range.
        high (int): Upper bound of the guessing range.

    Returns:
        int: Number of attempts.
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
            print(
                f"\n🎉 You got it in "
                f"{attempts} attempt{'s' if attempts != 1 else ''}!"
            )

            player_name = input(
                "Enter your name for the leaderboard: "
            ).strip()

            add_score(player_name, attempts)

            print("🏆 Score saved!")
            break

    return attempts


def main():
    """
    Entry point for the Number Guessing Game.
    """
    print("=" * 40)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 40)

    while True:
        play_game()

        display_leaderboard()

        again = input("\nPlay again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
