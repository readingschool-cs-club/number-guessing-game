#!/usr/bin/env python3
#
# A number guessing game.
#

from random import randint
from getpass import getpass

def read_num(prompt=None, func=input, default=None):
    if default is not None:
        if prompt.endswith(" "):
            prompt = prompt[:-1]
        prompt = prompt + " (default: %d): " % default

    while True:
        try:
            answer = func(prompt)
            if default is not None and not answer.strip():
                return default
            else:
                return int(answer)
        except ValueError:
            pass

def select(options, prompt="Choose: "):
    """Allow selection of a choice from a list"""
    for i, choice in enumerate(options):
        print("%d) %s" % (i + 1, choice[0]))

    while True:
        try:
            num = read_num(prompt)
            if num > 0:
                return options[num - 1][1]
        except IndexError:
            pass

def get_random_number():
    """Return a random integer."""
    lower_limit = read_num("What is the minimum? ", default=0)
    upper_limit = read_num("What is the maximum? ", default=10)

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
    print("How should I choose the number?")
    print("Pick a number: ")
    number_to_guess = select([
        ("I will choose it", get_user_number),
        ("Choose a random number", get_random_number),
    ])()

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
        print("It was %d!" % number_to_guess)

if __name__ == "__main__":
    main()
