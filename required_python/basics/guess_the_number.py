"""A tiny number guessing game for basics practice."""

from __future__ import annotations

import random


def play_game() -> None:
    """Let the player guess a number from 1 to 10."""

    secret_number = random.randint(1, 10)
    attempts = 3

    print("Guess a number from 1 to 10.")

    while attempts > 0:
        guess = int(input("Your guess: "))

        if guess == secret_number:
            print("Correct. You win.")
            return

        attempts -= 1

        if guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

        print(f"Attempts left: {attempts}")

    print(f"Game over. The number was {secret_number}.")


if __name__ == "__main__":
    play_game()