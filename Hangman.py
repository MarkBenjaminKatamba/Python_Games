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
    4. https://youtu.be/m4nEnsavl6w							
'''

import random
from AfricanCountries import Africa

def guess_word():
    secretWord = random.choice(Africa)                    # randomly choosing a word from the imported list
    return secretWord.upper()                                           # converting all user input to uppercase

# For the actual interactive game play, we need the function below, within
# which we'll create several variables that we'll be updating during each turn
# the user takes.
    
def GamePlay(secretWord):                                               # Display the secret word during each turn.
    wordCompletion = ' _ ' * len(secretWord)                            # So the secret word (unguessed letters) will initially be displayed as underscores
    guessed = False
    guessedLetters = []                                                 # This list will hold the letters the user guesses
    guessedWords = []                                                    # This will hold the words the user guesses
    trials = 6
    print("Welcome to the Hangman Game!")
    print("It consists of names of African countries, so you'll be guessing which country name you think is represented by the dashes below.")
    print("\n")
    print(wordCompletion)                                               # Printing the initial state of the game with all underscores
    print("\n")
    while not guessed and trials > 0:                                   # So we need a while loop that will run until either the word is guessed or the user runs out of guesses.
        guess = input("Please guess a letter or word (Hint: it's an African country): ").upper()
        if len(guess) == 1 and guess.isalpha():                         # Guessing a letter would mean that guess has a length of 1, and contains only characters from the alphabet
            if guess in guessedLetters:
                print("You already guessed the letter, ", guess)
            elif guess not in secretWord:
                print(guess, "is not in the word.")
                print("\n")
                trials -= 1
                guessedLetters.append(guess)
            else:
                print("Nice! ",guess, "is in the word!")
                guessedLetters.append(guess)
                word_2_list = list(wordCompletion)                      # Here, we're converting secretWord to a list in order to update out variable in order to reveal to the user all occurances of guess.
                indices = [i for i, letter in enumerate(secretWord) if letter == guess]
                for index in indices:
                    word_2_list[index] = guess
                wordCompletion = "".join(word_2_list)
                if "_" not in wordCompletion:
                    guessed = True
                
        elif len(guess) == len(secretWord) and guess.isalpha():         # Guessing a word will mean that the length of guess is equal to the length of the actual word and contains only alphabets.
            if guess in guessedWords:
                print("You already guessed the word ", guess)
            elif guess != secretWord:
                print(guess, " is not the word.")
                trials -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompletion = secretWord
                
        else: 
            print("Not a valid guess.")
        print(wordCompletion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You WIN!")
    else:
        print("Sorry, you ran out of trials. The word was " + secretWord + ". Maybe next time.")
'''
Each iteration of the loop coresponds to a new turn by the user
Inside this loop we'll have 3 possible conditional branches, each based on 
different user input: Guessing a letter, Guessing a word, or typing something 
other than a single letter or word of the correct length.
'''
def main():
    secretWord = guess_word()
    GamePlay(secretWord)
    while input("Play Again? (Y/N)").upper() == "Y":
        secretWord = guess_word()
        GamePlay(secretWord)


if __name__ == "__main__":
    main()
