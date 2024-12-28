# App name   => Password Generator 
# Programmer => Sam Kumbi
# Date       => Friday 12.27.2024

# App description
# ---------------
# This app generates 8 16-character passwords comprising of characters, numbers, lower and uppercase letters.
# Method 2

import random

PASSWORD_COUNT = 8

characters = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[','{',']','}','|',';',':',',','<','>','.','/','?', '\\']
numbers    = ['1','2','3','4','5','6','7','8','9','0']
uppercase  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

counter       = 0
number_list   = 1
password_bank = []

while counter < PASSWORD_COUNT:

    # Select and randomize 4 characters, 4 numbers, 3 lower and 5 uppercase letters from the lists
    random_chars = ''.join(random.sample(characters, 4))
    random_numbs = ''.join(random.sample(numbers,    4))
    random_upper = ''.join(random.sample(uppercase,  3))
    random_lower = ''.join(random.sample(lowercase,  5))

    # Concatenate the strings
    password = random_chars + random_numbs + random_upper + random_lower

    # Convert string to a list (since strings are immutable)
    password_list = list(password)

    # Randomize/shuffle the list items
    random.shuffle(password_list)

    # Convert the list back to a string
    final_password = ''.join(password_list)
    
    # Store password in password bank
    password_bank.append(final_password)
    
    counter += 1

# Welcome message
print("\nWelcome to Password Generator")
print("-----------------------------")
print("Here are eight suggestions for a strong password:\n")

# Display list of passwords
for password in password_bank:
    print(str(number_list) + ") " + f"{password}")
    number_list += 1
    
print()