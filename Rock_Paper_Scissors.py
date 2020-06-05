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
scores = 0
scores1 = 0

while gameRounds < 5:
    print("The game is Rock, Paper, Scissors; enter your guess: ")
    
    My_guess = input()
    Comp_guess = random.choice(Comp_Play)

    print(Comp_guess)

    if My_guess == 'rock' and Comp_guess == 'scissors':
        scores = scores + 5
        print('Rock crushes scissors, you WIN! ' + str(scores) + ' points for you!')

    elif My_guess == 'scissors' and Comp_guess == 'rock':
        scores1 = scores1 + 5
        print('Rock crushes scissors, you LOSE!')

    elif My_guess == 'paper' and Comp_guess == 'rock':
        scores = scores + 5
        print('Paper covers rock, you WIN! ' + str(scores) + ' points for you!')

    elif My_guess == 'rock' and Comp_guess == 'paper':
        scores1 = scores1 + 5
        print('Paper covers rock, you LOSE!')

    elif My_guess == 'scissors' and Comp_guess == 'paper':
        scores = scores + 5
        print('Scissor cuts paper, you WIN! ' + str(scores) + ' points for you!')

    elif My_guess == 'paper' and Comp_guess == 'scissors':
        scores1 = scores1 + 5
        print('Scissor cuts paper, you LOSE!')

    elif My_guess == Comp_guess:
        print('You tied! Replay to break the tie.')

    
    
    gameRounds = gameRounds + 1
    if gameRounds == 5:
        print('Game Over! Your total score is ' + str(scores) + ' points.')
        print("And your opponent's total score is " + str(scores1) + '.')
    
if scores > scores1:
   print('The game is yours: CONGRATULATIONS!!!')
elif scores < scores1:
  print("You lost this game, try again next time.")
elif scores == scores1:
    print("The game was a tie. Play it again.")
    