# Write a programme, which generates a random password for the user. 
# Ask the user how long they want their password to be, and how many 
# letters and numbers they want in their password. Have a mix of upper 
# and lowercase letters, as well as numbers and symbols. The password 
# should be a minimum of 6 characters long.

import random
import string

# pass_len = input("Enter the desired password length:\n")
# for pass_len in range (1,6):
#     if pass_len < 6:
#         print("Password cannot be less than 6 characters!")
#     break

# from functiontest import length
# import functiontest #custom module to handle the password character limit

# functiontest.pass_len



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
    ''.join(random.choice(pass_num1) for i in range(int(pass_num)))
    
    pass_sym1 = string.punctuation
    ''.join(random.choice(pass_sym1) for i in range(int(pass_sym)))
    
    pass_letters1 = string.ascii_letters
    ''.join(random.choice(pass_letters1) for i in range(int(pass_letters)))
    
    pass_char = pass_num1 + pass_sym1 + pass_letters1
    
    return ''.join(random.choice(pass_char) for i in range((int(length))))

print("Your new password is ", Password())

# Helpful References: 
#   1. shorturl.at/eBXYZ
#   2. shorturl.at/bzS29
#   3. shorturl.at/bmVX5
#   4. https://www.programiz.com/python-programming/modules
