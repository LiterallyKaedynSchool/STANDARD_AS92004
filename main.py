'''Simple Quiz
Kaedyn Eastall
Licensed with the JSS General Public License 001 - https://github.com/Jester-Software-Systems/JSS_LICENSE_DIRECTORY/blob/2025-Licenses/MARCH/JSS-GPL1
'''

# Import
import random
import os
import time

# Variables
INT_POINTS = 0
INT_LOSE = 2.5
INT_WIN = 5
bool_play_again = True
str_username = ""
int_question = 1
bool_playing = False
str_playing = ""

# Main Greeting

print("test")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def end():
    time.sleep(1.5)
    print("Goodbye!")
    exit()

def welcome(str_username):
    print("Hello, {}! Are you ready to play (Input yes or no)?".format(str_username))
    str_playing = input()
    str_playing.lower()
    if str_playing == "yes":
        bool_playing = True
        str_playing = "yes"
        clear()
    elif str_playing == "no":
        bool_playing = False
        print("Alright, thank you for testing.")
        end()
    else:
        print("Please input \"yes\" or \"no\"!")
        time.sleep(2)
        clear()
        welcome(str_username)

clear()
print("Hello, user! Welcome to the quiz, what is your name?")
str_username = input()
welcome(str_username)
