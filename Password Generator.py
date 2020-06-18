# Write a programme, which generates a random password for the user. 
# Ask the user how long they want their password to be, and how many 
# letters and numbers they want in their password. Have a mix of upper 
# and lowercase letters, as well as numbers and symbols. The password 
# should be a minimum of 6 characters long.

import random
import string

pass_len = input("Enter the desired password length:\n")

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
    
    return ''.join(random.choice(pass_char) for i in range(int(pass_len)))

print("Your new password is ", Password())

# letters = string.punctuation
# print ( ''.join(random.choice(letters) for i in range(10)) )