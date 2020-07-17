"""
Attempting the Password Generator, but this time using the random.sample() 
function instead of random.choice() in order to generate a password with 
non-repeating characters.
@author: kmark

Write a programme, which generates a random password for the user. 
Ask the user how long they want their password to be, and how many 
letters and numbers they want in their password. Have a mix of upper 
and lowercase letters, as well as numbers and symbols. The password 
should be a minimum of 6 characters long.
"""

import random
import string

def pass_len():
    global length 
    length = input("Enter the desired password length:\n")
    if int(length) < 6:
            print("Password cannot be less than 6 characters!!!")
            return pass_len()
pass_len()


def pass_numx():
    global pass_num
    pass_num = input("How many digits in password:\n")
    if int(pass_num) > int(length):
        print("Cannot be greater than overall password length!")
        return pass_numx()
    elif int(pass_num) == int(length):
        print("Cannot be equal to overall password length!")
        return pass_numx()
pass_numx()
                 


def pass_symx():
    global pass_sym 
    pass_sym = input("How many symbols in password:\n")
    if int(pass_sym) > int(length):
        print("Cannot be greater than overall password length!")
        return pass_symx()
    elif int(pass_sym) == int(length):
        print("Cannot be equal to overall password length!")
        return pass_symx()
pass_symx()



def pass_lettersx():
    global pass_letters 
    pass_letters = input("How many letters in password:\n")
    if int(pass_letters) > int(length):
        print("Cannot be greater than overall password length!")
        return pass_lettersx()
    elif int(pass_letters) == int(length):
        print("Cannot be equal to overall password length!")
        return pass_lettersx()
pass_lettersx()
 

def Password():
    
    pass_num1 = string.digits
    p_n = ''.join(random.choice(pass_num1) for i in range(int(pass_num)))
    
    pass_sym1 = string.punctuation
    p_s = ''.join(random.choice(pass_sym1) for i in range(int(pass_sym)))
    
    pass_letters1 = string.ascii_letters
    p_l = ''.join(random.choice(pass_letters1) for i in range(int(pass_letters)))
    
    pass_char = p_n + p_s + p_l  
#    print(pass_char)
    return ''.join((random.sample(pass_char, int(length))))

if int(pass_num) + int(pass_sym) + int(pass_letters) != int(length):
    print("Sorry, your password character count does not add up, please check your inputs and try again.")
elif int(pass_num) + int(pass_sym) + int(pass_letters) == int(length):
    print("Your new password is ", Password())

""" Helpful References: 
   1. https://pynative.com/python-generate-random-string/
"""

