'''
This is probably the hardest one out of these 6 small projects. 
This will be similar to guessing the number, except we are guessing the word. 
The user needs to guess letters, Give the user no more than 6 attempts for 
guessing wrong letter. This will mean you will have to have a counter. 
You can download a ‘sowpods’ dictionary file or csv file to use as a way to 
get a random word to use.
===============================================================================
Useful Resource Links:
    1. https://thewordsearch.com/hangman
    2. https://en.wikipedia.org/wiki/Hangman_(game)
    3. a) https://www.downloadexcelfiles.com/wo_en/download-excel-file-list-african-countries-dependent-territories#.XvC3yGgzbDc 
       b) en.wikipedia.org/wiki/List_of_African_countries_by_population							
'''

import random
import string
import AfricanCountries.csv

def guess_word():
    secretWord = random.choice(AfricanCountries.csv) # randomly choosing a word from the imported list
    return secretWord.upper()       # converting all user input to uppercase

# For the actual interactive game play, we need the function below, within
# which we'll create several variables that we'll be updating during each turn
# the user takes.
    
def GamePlay(secretWord):
    wordCompletion = ' _ ' * len(secretWord) # So the secret word will initially contain only underscores
    guessed = False
    guessedLetters = []     # This list will hold the letters the user guesses
    guessedWord = []        # This will hold the words the user guesses
    Trials = 6
    print("Let's play Hangman!")
    print(wordCompletion)   # Printing the initial state of the game with all underscores
    print("\n")
# So we need a while loop that will run until either the word is guessed or the user runs out of guesses.    
    




    