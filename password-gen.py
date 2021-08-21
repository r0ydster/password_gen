#!/usr/bin/env python3

'''
Python Password Generator
Ask for the number of characters wanted in a Password, take that number,
generate a password randomizing letters, numbers and special characters.
'''

import string
import random
import sys

def main():
    print('Python Password Generator\n')

    # Prompt for length of password. 
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

    # Infinite loop
    choice = input('Press enter to generate another password or q to quit: ')
    if choice == 'q':
        sys.exit(0)
    else:
        main()

if __name__ == "__main__":
    main()
