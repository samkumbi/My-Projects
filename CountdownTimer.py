# App name   => Countdown Timer
# Programmer => Sam Kumbi

# App description
# ---------------
# This app prompts a user for time in seconds and counts down till it reaches zero.

import time

print("This program will countdown to zero from a time (in seconds) you provide.")

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Time's up!")

user_time = int(input("Enter seconds: "))

countdown(user_time)