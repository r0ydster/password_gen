#!/usr/bin/env python3

'''
Password generator
Prompt for number of characters in Password take that number, then generate a password randomizing letters, numbers and special characters.
'''

import string
import random

# Prompt for length of password, convert to int.

print('Python Password Generator\n')
length = int(input('Enter the length of the password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Combine all types 
all = lower + upper + num + symbols

# randomize all 
temp = random.sample(all,length)

# Create the password
password = "".join(temp)

# Print the generated password
print(password)