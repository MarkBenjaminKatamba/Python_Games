
import random

compPlay = ['rock', 'Rock', 'ROCK', 'paper', 'Paper', 'PAPER', 'scissors', 'Scissors', 'SCISSORS']
gameRounds = 0
myScore = 0
compScore = 0

while gameRounds < 5:
    print("The game is Rock, Paper, Scissors; enter your guess: ")
    myGuess = str(input())
    compGuess = random.choice(compPlay)

    if myGuess == 'rock' and compGuess == 'scissors':
        print(compGuess)
        myScore += 5
        print(f'Rock crushes scissors, you WIN {myScore} points for that! \n')

    elif myGuess == 'Rock' and compGuess == 'Scissors':
        print(compGuess)
        myScore += 5
        print(f'Rock crushes scissors, you WIN {myScore} points for that! \n')

    elif myGuess == 'ROCK' and compGuess == 'SCISSORS':
        print(compGuess)
        myScore += 5
        print(f'Rock crushes Scissors, you WIN {myScore} points for that! \n')

    elif myGuess == 'rock' and compGuess == 'scissors':
        print(compGuess)
        myScore += 5
        print(f'Rock crushes Scissors, you WIN {myScore} points for that! \n')

    elif myGuess == 'ROCK' and compGuess == 'scissors':
        print(compGuess)
        myScore += 5
        print(f'Rock crushes Scissors, you WIN {myScore} points for that! \n')

    elif myGuess == 'rock' and compGuess == 'SCISSORS':
        print(compGuess)
        myScore += 5
        print(f'Rock crushes Scissors, you WIN {myScore} points for that! \n')

    elif myGuess == 'Rock' and compGuess == 'scissors':
        print(compGuess)
        myScore += 5
        print(f'Rock crushes Scissors, you WIN {myScore} points for that! \n')

    elif myGuess == 'rock' and compGuess == 'Scissors':
        print(compGuess)
        myScore += 5
        print(f'Rock crushes Scissors, you WIN {myScore} points for that! \n')

# =========================================================================================

    elif myGuess == 'scissors' and compGuess == 'rock':
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    elif myGuess == 'Scissors' and compGuess == 'Rock':
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    elif myGuess == 'SCISSORS' and compGuess == 'ROCK':
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    elif myGuess == 'scissors' and compGuess == 'ROCK':
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    elif myGuess == 'SCISSORS' and compGuess == 'rock':
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    elif myGuess == 'Scissors' and compGuess == 'ROCK':
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    elif myGuess == 'SCISSORS' and compGuess == 'Rock':
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    elif myGuess == 'Scissors' and compGuess == 'rock':
        print(compGuess)
        compScore += 5
        print('Rock crushes scissors, you lose! \n')

    # =========================================================================================

    elif myGuess == 'paper' and compGuess == 'rock':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == 'Paper' and compGuess == 'Rock':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == 'PAPER' and compGuess == 'ROCK':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == 'Paper' and compGuess == 'ROCK':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == 'paper' and compGuess == 'Rock':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == 'paper' and compGuess == 'ROCK':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == 'PAPER' and compGuess == 'Rock':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == 'Paper' and compGuess == 'rock':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

    elif myGuess == 'PAPER' and compGuess == 'rock':
        print(compGuess)
        myScore += 5
        print(f'Paper covers rock, you WIN! {myScore} points for that! \n')

# ==================================================================================================

    elif myGuess == 'scissors' and compGuess == 'paper':
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

    elif myGuess == 'Scissors' and compGuess == 'Paper':
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

    elif myGuess == 'SCISSORS' and compGuess == 'PAPER':
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

    elif myGuess == 'SCISSORS' and compGuess == 'Paper':
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

    elif myGuess == 'Scissors' and compGuess == 'PAPER':
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

    elif myGuess == 'SCISSORS' and compGuess == 'paper':
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

    elif myGuess == 'scissors' and compGuess == 'PAPER':
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

    elif myGuess == 'scissors' and compGuess == 'Paper':
        print(compGuess)
        myScore += 5
        print(f'Scissor cuts paper, you WIN! {myScore} points for that! \n')

# =========================================================================================

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
