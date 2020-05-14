# Make a rock-paper-scissors game where it is the player vs the computer. 
# The computer’s answer will be randomly generated, while the program will ask the user for their input. 
# This project will better your understanding of while loops and if statements.

# How to use random.choice() function to randomly select things from a list (Resource: https://pynative.com/python-random-choice/)
# import random
# movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']

# moview_item = random.choice(movie_list)
# print ("Randomly selected item from list is - ", moview_item)

# moview_item = random.choice(movie_list)
# print ("Randomly selected item from list is - ", moview_item)

import random
Comp_Play = ['rock', 'paper', 'scissors']
gameRounds = 0

while gameRounds < 5:
    print("The game is Rock, Paper, Scissors; enter your guess: ")
    
    My_guess = input()
    Comp_guess = random.choice(Comp_Play)

    print(Comp_guess)

    if My_guess == 'rock' and Comp_guess == 'scissors':
        print('Rock crushes scissors, you WIN!')

    elif My_guess == 'scissors' and Comp_guess == 'rock':
        print('Rock crushes scissors, you LOSE!')

    elif My_guess == 'paper' and Comp_guess == 'rock':
        print('Paper covers rock, you WIN!')

    elif My_guess == 'rock' and Comp_guess == 'paper':
        print('Paper covers rock, you LOSE!')

    elif My_guess == 'scissors' and Comp_guess == 'paper':
        print('Scissor cuts paper, you WIN!')

    elif My_guess == 'paper' and Comp_guess == 'scissors':
        print('Scissor cuts paper, you LOSE!')

    elif My_guess == Comp_guess:
        print('You tied! Replay to break the tie.')

    gameRounds = gameRounds + 1
    if gameRounds == 5:
        print('Game Over, count the points.')
