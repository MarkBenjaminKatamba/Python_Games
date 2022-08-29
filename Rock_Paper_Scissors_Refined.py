# Make a rock-paper-scissors game where it is the player vs the computer.
# The computer's answer will be randomly generated, while the program will
# ask the user for their input.
# This project will better your understanding of while loops and if statements.

# How to use random.choice() function to randomly select things from a list
# (Resource: https://pynative.com/python-random-choice/)
# import random
# movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']

# moview_item = random.choice(movie_list)
# print ("Randomly selected item from list is - ", moview_item)

# moview_item = random.choice(movie_list)
# print ("Randomly selected item from list is - ", moview_item)

import random

compPlay = ['rock', 'Rock', 'paper', 'Paper', 'scissors', 'Scissors']
gameRounds = 0
myScore = 0
compScore = 0

while gameRounds < 5:
    print("The game is Rock, Paper, Scissors; enter your guess: ")
    myGuess = input()
    compGuess = random.choice(compPlay)
    print("Opponent's guess: " + compGuess)

    # if myGuess is not compPlay:
    #    print("Wrong input. Please enter either 'rock', 'paper', or 'scissors'")
    #     # return myGuess

    if myGuess == 'rock' or 'Rock' and compGuess == 'scissors' or 'Scissors':
        myScore += 5
        print('Rock crushes scissors, you WIN! ' + str(myScore) + ' points for you!')
        print('\n')

    elif myGuess == 'scissors' or 'Scissors' and compGuess == 'rock' or 'Rock':
        compScore += 5
        print('Rock crushes scissors, you LOSE!')
        print('\n')

    elif myGuess == 'paper' or 'Paper' and compGuess == 'rock' or 'Rock':
        myScore += 5
        print('Paper covers rock, you WIN! ' + str(myScore) + ' points for you!')
        print('\n')

    elif myGuess == 'rock' or 'Rock' and compGuess == 'paper' or 'Paper':
        compScore += 5
        print('Paper covers rock, you LOSE!')
        print('\n')

    elif myGuess == 'scissors' or 'Scissors' and compGuess == 'paper' or 'Paper':
        myScore += 5
        print('Scissor cuts paper, you WIN! ' + str(myScore) + ' points for you!')
        print('\n')

    elif myGuess == 'paper' or 'Paper' and compGuess == 'scissors' or 'Scissors':
        compScore += 5
        print('Scissor cuts paper, you LOSE!')
        print('\n')

    elif myGuess == compGuess:
        print('You tied! Replay to break the tie.')
        print('\n')

gameRounds += 1
if gameRounds == 5:
    print('Game Over! Your total score is ' + str(myScore) + ' points.')
    print("And your opponent's total score is " + str(compScore) + '.')
    print('\n')

if myScore > compScore:
    print('The game is yours: CONGRATULATIONS!!!')
elif myScore < compScore:
    print("You lost this game, try again next time.")
elif myScore == compScore:
    print("The game was a tie. Wanna give it another try?")
