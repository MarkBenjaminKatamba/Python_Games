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



def pass_numx():
    global pass_num
    pass_num = input("How many digits in password:\n")
    if int(pass_num) > int(length):
        print("Cannot be greater than overall password length!")
    elif int(pass_num) == int(length):
        print("Cannot be equal to overall password length!")
    return pass_numx()
pass_numx()
                 


def pass_symx():
    global pass_sym 
    pass_sym = input("How many symbols in password:\n")
    if int(pass_sym) > int(length):
        print("Cannot be greater than overall password length!")
    elif int(pass_sym) == int(length):
        print("Cannot be equal to overall password length!")
        return pass_symx()
pass_symx()



def pass_lettersx():
    global pass_letters 
    pass_letters = input("How many letters in password:\n")
    if int(pass_letters) > int(length):
        print("Cannot be greater than overall password length!") 
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

    return ''.join((random.choice(pass_char) for i in range(int(length))))
print("Your new password is ", Password())


'''
Note that some characters will repeat themselves, since we used random.choice. 
To achieve a password with non-repeating characters, we'd use random.sample, 
though this is not recommended in real life.
Helpful References: 
===================
   1. https://pynative.com/python-generate-random-string/
   2. https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=edpresso-dynamic&gclid=EAIaIQobChMI9bjDysOr6QIVRe7tCh2V1wNxEAAYASAAEgJVnfD_BwE
   3. shorturl.at/bmVX5
   4. https://www.programiz.com/python-programming/modules
'''