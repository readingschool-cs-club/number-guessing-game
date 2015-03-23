#!/usr/bin/env python3
#
# A number guessing game.
#

from random import randint
from getpass import getpass

def read_num(prompt=None, func=input):
    while True:
        try:
            return int(func(prompt))
        except ValueError:
            pass

def get_number_to_guess():
    """Return the number for Player 2 to guess."""
    #num = get_random_number()
    num = get_user_number()
    return num

def get_random_number():
    """Return a random integer."""
    lower_limit = 0
    upper_limit = 10

    num = randint(lower_limit, upper_limit)

    return num

def get_user_number():
    """Prompt for and return a valid integer given by Player 1."""
    # don't echo so only Player 1 knows what they entered
    num = read_num("Please enter a number: ", getpass)

    return num

def get_guess():
    """Prompt Player 2 for an valid integer and return it."""
    guess_num = read_num("Please enter your guess: ")
    return guess_num

def get_higher_lower_hint(number_to_guess, guess):
    """Return a word which describes the where the number to guess is on
    the number line relative to the given guess."""
    HIGHER = "higher than"
    LOWER = "lower than"
    SAME = "the same as"

    if number_to_guess > guess:
        return HIGHER
    elif number_to_guess < guess:
        return LOWER
    else:
        # sanity check: return 'same as' if they're the same
        # this function shouldn't be called if that's the case, but
        # better safe than sorry!
        return SAME


def main():
    # set initial game state
    max_guesses = 3
    number_to_guess = get_number_to_guess()

    # declare & initialise some variables to use in the while loop
    guesses_taken = 0
    guessed_correctly = False

    while not guessed_correctly and guesses_taken < max_guesses:
        # get another guess from Player 2
        guess = get_guess()

        # increment guesses taken
        guesses_taken += 1

        # check if Player 2 guessed correctly
        if guess == number_to_guess:
            guessed_correctly = True
            # exit while loop early (not actually required, but shows
            # program flow more clearly)
            break
        else:
            # they didn't: give them a hot/cold hint
            print("Nope! That's not it.")
            adj = get_higher_lower_hint(number_to_guess, guess)
            print("The number to guess is %s that." % adj)

    # game has ended: print some messages based on the outcome
    if guessed_correctly:
        print("You got it right!")
    elif guesses_taken == max_guesses:
        print("You ran out of guesses...")

if __name__ == "__main__":
    main()
