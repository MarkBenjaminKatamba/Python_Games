# # Working with While loops (Resource: https://www.digitalocean.com/community/tutorials/how-to-construct-while-loops-in-python-3)

# password = ''
# while password != 'Naggie':
#     print('What is the password?')
#     password = input()
    
# print('Yes, the password is ' + password + '. You may enter.')

# # Random string generator: https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=edpresso-dynamic&gclid=EAIaIQobChMI9bjDysOr6QIVRe7tCh2V1wNxEAAYASAAEgJVnfD_BwE

# ==========================================================================
# import random
# import string

# # printing lowercase
# letters = string.ascii_lowercase
# print ( ''.join(random.choice(letters) for i in range(10)) )

# # printing uppercase
# letters = string.ascii_uppercase
# print ( ''.join(random.choice(letters) for i in range(10)) )

# # printing letters
# letters = string.ascii_letters
# print ( ''.join(random.choice(letters) for i in range(10)) )

# # printing digits
# letters = string.digits
# print ( ''.join(random.choice(letters) for i in range(10)) )

# # printing punctuation
# letters = string.punctuation
# print ( ''.join(random.choice(letters) for i in range(10)) )
# ========================================================================


# import random
# import string

# def randomStringwithDigitsAndSymbols(stringLength=10):
#     password_characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choice(password_characters) for i in range(stringLength))

# print("Generating Random String password with letters, digits and special characters ")
# print ("First Random String ", randomStringwithDigitsAndSymbols() )
# print ("Second Random String", randomStringwithDigitsAndSymbols(10) )
# print ("Third Random String", randomStringwithDigitsAndSymbols(10) )



import random
import string

def randString(length=5):
    # put your letters in the following string
    your_letters='abcdefghi'
    return ''.join((random.choice(your_letters) for i in range(length)))

print("Random String with specific letters ", randString())
print("Random String with specific letters ", randString(5))