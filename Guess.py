# Working with While loops 
# (Resource: https://www.digitalocean.com/community/tutorials/how-to-construct-while-loops-in-python-3)

import random

number = random.randint(1, 25)

number_of_guesses = 0

while number_of_guesses < 5:
    print('Guess a number between 1 and 25:')
    guess = input()
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1

    if number > guess > 1:
        print('Your guess is too low')

    if number < guess < 25:
        print('Your guess is too high')

    # if 25 < guess < 1:
    #     print('Your guess is out of range!')

    if guess < 1:
        print('Your guess is out of range!')

    if guess > 25:
        print('Your guess is out of range!')

    if guess == number:
        break

if guess == number:
    print('Nice! You guessed the number on the ' + str(number_of_guesses) + 'th trial!')

else:
    print('You did not guess the number. The number was ' + str(number))
