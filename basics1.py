# App name   => Basics1
# Programmer => Sam Kumbi

# App description
# ---------------
# Learning the basics of Python.

import math

#end = 100
#count = 0

#while(count < end):
#    count+=1
#    print(count)

# print(math.sqrt(16))
# print(math.remainder(10, 7))
def add(first_number, second_number):
    return first_number + second_number

user_input = input("Enter first number: ")
fir_num    = int(user_input)
user_input = input("Enter second number: ")
sec_num    = int(user_input)

total = add(fir_num, sec_num)

print("Total: " + str(total))