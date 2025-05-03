'''
Quiz about New Zealand
Kaedyn Eastall
Licensed with the JSS General Public License 001 - https://github.com/Jester-Software-Systems/JSS_LICENSE_DIRECTORY/blob/2025-Licenses/MARCH/JSS-GPL1
'''
import time # 'time' has been imported so I can make the user wait a certain amount of seconds
import os # 'os' has been imported so I can clear the screen on game restart

# Lists & Variables
int_score = 0 # Setting the 'int_score' variable to 0
int_question = 0 # Setting the user on question 0
str_name = "" # Setting the user name to blank before they input it.
LIST_QUESTIONS = [ # A list with all the questions
    "What british sailor officially mapped New Zealand?",
    "What is the capital of New Zealand?",
    "Where is the big carrot?",
    "What is the name of the glowworm caves on the North Island?",
    "What is the name of this 328m high landmark in Auckland?",
    "Can you name the highest mountain in New Zealand?",
    "(True or False) The South Island the largest island in the world?",
    "What does the māori word \"Taraka\" mean?"
]
LIST_ANSWERS = [ # Alist with all the answers
    "James Cook",
    "Wellington",
    "Ohakune",
    "Waitomo",
    "Sky Tower",
    "Mount Cook",
    "False",
    "Truck"
]
LIST_CHAT = [ # A list with all the other things I have to say.
    "Welcome to Kaedyn's quiz! Whats your name?",
    "Ok! Please wait three seconds and then the quiz will restart.",
    "Alright, thanks for playing!"
]

# Intro & Question Print Loop
print(LIST_CHAT[0])
str_name = input() # User name input
def playing():
    global int_score
    for i in range (len(LIST_QUESTIONS)):
        time.sleep(1)
        print("\n")
        print(f"{LIST_QUESTIONS[i]}")
        ans = input()
        ans = ans.lower().title()
        if ans == LIST_ANSWERS[i]:
            int_score += 5
            print(f"✅  That's right! You now have {int_score} points.")
            i =+ 1
        else: 
            int_score -= 2.5
            print(f"❌  That's wrong. The answer was {LIST_ANSWERS[i]}.\nYou now have {int_score} points.")
            i =+ 1

def runit():
    global int_score
    time.sleep(1)
    print("\n")
    print(f"Alright, {str_name}. You finished with {int_score}/40 points! Want to try again?")
    tryagain = input()
    tryagain = tryagain.lower().title()
    if tryagain == "Yes":
        print(LIST_CHAT[1])
        int_question = 0
        int_score = 0
        time.sleep(3)
        os.system('clear')
        playing()
    elif tryagain == "No":
        print(LIST_CHAT[2])
        quit()
    else:
        print(f"Hey! {str_name}! It's a yes or no question!")
        time.sleep(1)
        runit()
playing()
runit()
