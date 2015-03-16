#!/usr/bin/env python3
#
# A number guessing game.
#

maximum_guesses = 10

number_to_guess = input("Please enter a number: ")

guess_taken = 0
while guess != number_to_guess and guesses_taken < maximum_guesses:
  guesses_taken += 1
  guess = input("Please enter your guess: ")

if guess == number_to_guess:
  print("You got it right!")
elif guesses_taken == maximum_guesses:
  print("You ran out of guesses...")
