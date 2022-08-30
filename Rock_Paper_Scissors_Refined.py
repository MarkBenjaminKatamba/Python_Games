
import random

compPlay = ['rock', 'Rock', 'ROCK', 'paper', 'Paper', 'PAPER', 'scissors', 'Scissors', 'SCISSORS']
gameRounds = 0
myScore = 0
compScore = 0

while gameRounds < 5:
    print("The game is Rock, Paper, Scissors; enter your guess: ")
    myGuess = str(input())
    compGuess = random.choice(compPlay)

    if myGuess == ('rock' or 'Rock' or 'ROCK') and compGuess == ('scissors' or 'Scissors' or 'SCISSORS'):
        print(compGuess)
        myScore += 5
        print(f'Rock crushes scissors, you WIN {myScore} points for that! \n')

    elif myGuess == ('scissors' or 'Scissors' or 'SCISSORS') and compGuess == ('rock' or 'Rock' or 'ROCK'):
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    elif myGuess == ('paper' or 'Paper' or 'PAPER') and compGuess == ('rock' or 'Rock' or 'ROCK'):
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == ('rock' or 'Rock' or 'ROCK') and compGuess == ('paper' or 'Paper' or 'PAPER'):
        print(compGuess)
        compScore += 5
        print('Paper covers rock, you lose! \n')

    elif myGuess == ('scissors' or 'Scissors' or 'SCISSORS') and compGuess == ('paper' or 'Paper' or 'PAPER'):
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

    elif myGuess == ('paper' or 'Paper' or 'PAPER') and compGuess == ('scissors' or 'Scissors' or 'SCISSORS'):
        print(compGuess)
        compScore += 5
        print('Scissor cuts paper, you lose! \n')

    elif myGuess == compGuess:
        print(compGuess)
        print('You tied on this one! \n')

    elif myGuess not in compPlay:
        print('Invalid Input!')


if gameRounds == 5:
    print(f'Game Over! \n Your total score is {myScore} points.')
    print(f"And Lenovo's total score is {compScore} points\n")

    if myScore > compScore:
        print("CONGRATULATIONS! This game is yours.")
    if myScore < compScore:
        print("Sorry, you lost this game. Wanna try again?")
    if myScore == compScore:
        print(f"You both scored {myScore} points. Wanna try again?")
