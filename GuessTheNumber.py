# App name   => Guess the Number 
# Programmer => Sam Kumbi

# App description
# ---------------
# This game prompts the user to guess a randomly generated number between 1 and 10

import random

print("Guess the correct number. Enter a number between 1 and 10")

random_number = random.randint(1,10)
user_value = 0
counter    = 0

while (user_value != random_number):
    user_value = int(input("> "))
    
    if (user_value == random_number and counter == 0):
        print("\n" + str(user_value) + " is correct! You got it right on the first try. You must be a genius!\n")
        print("Thanks for playing!\n")
        break
    
    counter += 1
    
    if (user_value == random_number):
        print("\n" + str(user_value) + " is correct! It took you " + str(counter) + " guesses.\n")
        print("Thanks for playing!\n")
        break
    
    print("Try again!\n")