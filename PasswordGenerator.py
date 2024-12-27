# App name   => Password Generator 
# Programmer => Sam Kumbi
# Date       => Friday 12.27.2024

# App description
# ---------------
# This app generates 8 16-character passwords comprising of characters, numbers, lower and uppercase letters.
# Method 1

import random
import string

PASSWORD_COUNT = 8

all_characters = list(string.ascii_letters + string.digits + string.punctuation)

counter       = 0
number_list   = 1
password_bank = []

while (counter < PASSWORD_COUNT):

    # Select and randomize characters, numbers, lower and uppercase letters from the arrays
    random_chars = ''.join(random.sample(all_characters, 16))

    # Convert string to a list (since strings are immutable)
    password_list = list(random_chars)

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