# Guess The Number
# Write a programme where the computer randomly generates a number between 0 and 20. The user needs to 
# guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. 
# This will get you started with the random library if you haven't already used it.

import random
# # Printing random number
# print("Random Number: ")
# print(random.random())

print("Computer generates random number here... \n")
comp_num = random.randint(1,20)         # Computer generates random number

guess_num = input("Guess random number between 1 and 20:  ")          # User guesses and inputs random number
guess_num = int(guess_num)
                           
# for num in comp_num:                 # If the user-guessed number, say x, is higher or lower than num,
if guess_num > comp_num and guess_num < 20:
    print("Your guess is too High!")
elif guess_num < comp_num and guess_num > 1:
    print("Your guess is too Low!")                           # print "Your Guess is too High" or "Your Guess is too Low" respectively
elif guess_num == comp_num:
    print("You guessed just right, that's the number!")
elif guess_num < 1:
    print("Sorry, your guess is out of the game range.")
elif guess_num > 20:
    print("Sorry, your guess is out of the game range.")