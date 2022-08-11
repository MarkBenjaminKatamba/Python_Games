"""
Reference tutorial: https://youtu.be/4s7fzzZNeHw

"""

import random
from AfricanCountries import Africa

# Set up the list of secret words
hiddenWord = (random.choice(Africa)).upper()
hidden = "_ " * len(hiddenWord)
guessedLetters = []
guessedWords = []
attempts = 6




# Loop until either the player wins or loses.
isGameOver = False

    # Display the current board,guessed letters/word, and tries remaining.

    # Ask the player for a character

    # If the player guessed correct, print success message and show all matched letters

    # If the player guessed wrong, print failure message and increment tries

    # IF the player has won, print a win message and stop looping

    # If the player has lost, print a lose message and stop looping