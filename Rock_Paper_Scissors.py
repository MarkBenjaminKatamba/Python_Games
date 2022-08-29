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

import random

Comp_Play = ['rock', 'paper', 'scissors']
gameRounds = 0
my_score = 0
comp_score = 0

while gameRounds < 5:
    print("The game is Rock, Paper, Scissors; enter your guess below: ")
    My_guess = input()
    Comp_guess = random.choice(Comp_Play)

    gameRounds = gameRounds + 1

    if My_guess == 'rock' and Comp_guess == 'scissors':
        print(Comp_guess)
        print('Rock crushes scissors, you WIN.')
        my_score += 5
        print(f'{my_score} points for that! \n')

    elif My_guess == 'scissors' and Comp_guess == 'rock':
        print(Comp_guess)
        print('Rock crushes scissors, you LOSE! \n')
        comp_score += 5

    elif My_guess == 'paper' and Comp_guess == 'rock':
        print(Comp_guess)
        print('Paper covers rock, you WIN!')
        print(f'Now you have {my_score + 5} points! \n')

    elif My_guess == 'rock' and Comp_guess == 'paper':
        print(Comp_guess)
        print('Paper covers rock, you LOSE! \n')
        comp_score += 5

    elif My_guess == 'scissors' and Comp_guess == 'paper':
        print(Comp_guess)
        print('Scissor cuts paper, you WIN!')
        print(f'Now you have {my_score + 5} points! \n')

    elif My_guess == 'paper' and Comp_guess == 'scissors':
        print(Comp_guess)
        print('Scissor cuts paper, you LOSE! \n')
        comp_score += 5

    elif My_guess == Comp_guess:
        print(Comp_guess)
        print('You tied on this one! \n')

    elif My_guess != Comp_Play:
        print('Invalid input. \n')
    #    break


if gameRounds == 5:
    print(f'Game Over! Your total score is {my_score} points.')
    print(f"And Lenovo's total score is {comp_score}. points\n")
    
    if my_score > comp_score:
        print("CONGRATULATIONS! This game is yours.")
    if my_score < comp_score:
        print("Sorry, you lost this game. Want to try again?")
    if my_score == comp_score:
        print(f"You both scored {my_score} points. Wanna try again to break the tie?")
