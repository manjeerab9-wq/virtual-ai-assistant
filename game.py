"""Number guessing game."""

import random

LOWEST_NUMBER = 1
HIGHEST_NUMBER = 20
MAX_ATTEMPTS = 5


def play_guessing_game(input_func=input, output_func=print, rng=random):
    """Run a guessing game and return when the user wins or runs out of attempts."""
    secret = rng.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
    output_func(
        f"I'm thinking of a number between {LOWEST_NUMBER} and {HIGHEST_NUMBER}. "
        f"You have {MAX_ATTEMPTS} tries."
    )
    for attempt in range(1, MAX_ATTEMPTS + 1):
        raw_guess = input_func(f"Guess {attempt}/{MAX_ATTEMPTS}: ").strip()
        try:
            guess = int(raw_guess)
        except ValueError:
            output_func("Please enter a whole number. This attempt counts.")
            continue
        if guess == secret:
            output_func(f"Correct! You got it in {attempt} attempt(s).")
            return True
        if guess < secret:
            output_func("Higher!")
        else:
            output_func("Lower!")
    output_func(f"Game over — the number was {secret}.")
    return False
