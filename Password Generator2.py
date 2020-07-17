"""
Created on Mon Jun 22 10:38:19 2020
Attempting the Password Generator, but this time using the random.sample() 
function instead of random.choice() in order to generate a password with 
non-repeating characters.
@author: kmark
"""
# Write a programme, which generates a random password for the user. 
# Ask the user how long they want their password to be, and how many 
# letters and numbers they want in their password. Have a mix of upper 
# and lowercase letters, as well as numbers and symbols. The password 
# should be a minimum of 6 characters long.

import random
import string

def pass_len():
    global length 
    length = input("Enter the desired password length:\n")
    if int(length) < 6:
            print("Password cannot be less than 6 characters!!!")
            return pass_len()
pass_len()


pass_num = input("How many digits in password:\n")
                 
pass_sym = input("How many symbols in password:\n")

pass_letters = input("How many letters in password:\n") 

def Password():
    
    pass_num1 = string.digits
    p_n = ''.join(random.choice(pass_num1) for i in range(int(pass_num)))
    
    pass_sym1 = string.punctuation
    p_s = ''.join(random.choice(pass_sym1) for i in range(int(pass_sym)))
    
    pass_letters1 = string.ascii_letters
    p_l = ''.join(random.choice(pass_letters1) for i in range(int(pass_letters)))
    
    pass_char = p_n + p_s + p_l  
    print(pass_char)
    return ''.join((random.sample(pass_char, int(length))))

print("Your new password is ", Password())

# Helpful References: 
#   1. https://pynative.com/python-generate-random-string/

