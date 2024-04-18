
# Code to generate random password.

import random

print('Your password: ')

# Generate list of passwords from random characters.
chars = 'adcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()'

# Declare password variable as a blank string.
password = ''

# For loop for the range of 16, which is the lenght of the password.
for x in range(16):

     password += random.choice(chars)

print(password)
