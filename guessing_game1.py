""" Guessing game - Justine Lee """

# adds random number functionality
import random

number_to_guess = random.randint(1,10)

# Set a boolean variable
keep_guessing = True

# Start a while loop, enabling guesses to be made
while keep_guessing == True:
    # Get the number (integer) that is to be guessed
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

    # If the guess is wrong, say "Incorrect", and repeat
    # If the guess is correct, end the loop and say "Correct"

    if guess == number_to_guess:
        print("Correct")
        keep_guessing = False
    elif guess > number_to_guess:
        print("Guess is too high,try again")
    else:
        print("Guess is too low, try again")
