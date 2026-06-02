# guessing_game.py
# Author: Raj Modi
# Date: June 2026
# Description:
# A number guessing game that helps practice user input,
# conditional statements, and problem-solving skills.

secret_number = 7

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct! You guessed the number.")
else:
    print("Not quite. Try again.")
