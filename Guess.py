# Working with While loops 
# (Resource: https://www.digitalocean.com/community/tutorials/how-to-construct-while-loops-in-python-3)

import random

number = random.randint(1, 30)

number_of_guesses = 0

while number_of_guesses < 10:
    print('Guess a number between 1 and 30:')
    guess = input()
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1

    if guess < 1 or guess > 30:
        print("Your guess is out of range.")

    elif guess < number:
        print('Your guess is too low')

    elif guess > number:
        print('Your guess is too high')

    elif guess == number:
        break

if guess == number:
    print('CONGRATULATIONS! You guessed the number in ' + str(number_of_guesses) + ' tries!')

if guess == number:
    print('Congratulations, You guessed the number in ' + str(number_of_guesses) + ' tries!!!')
else:
    print('You did not guess the number. The number was ' + str(number))

