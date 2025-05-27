'''
Quiz about New Zealand
Kaedyn Eastall
Licensed with the JSS General Public License 001 - https://github.com/Jester-Software-Systems/JSS_LICENSE_DIRECTORY/blob/2025-Licenses/MARCH/JSS-GPL1
'''
import time # 'time' has been imported so I can make the user wait a certain amount of seconds.
import os # 'os' has been imported so I can clear the screen on game restart.

# Lists & Variables
int_score = 0 # Setting the 'int_score' variable to 0.
int_question = 0 # Setting the user on question 0.
str_name = "" # Setting the user name to blank before they input it.
INT_PASSING_SCORE = 20 # The score you need to pass.

LIST_VALID_ANSWERS = [ "A", "B", "C", "D"] # A list of all the valid answers.
LIST_QUESTIONS = [ # A list with all the questions
    "What british sailor officially mapped New Zealand?\nA. James Cook\nB. Ernest Rutherford\nC. Dame Whina Cooper\nD. Richard Seddon",
    "What is the capital of New Zealand?\nA. Auckland\nB. Wellington\nC. Christchurch\nD. Taupō",
    "Where is the big carrot?\nA. Ohakune\nB. Masterton\nC. Foxton\nD. Waiouru",
    "What is the name of the glowworm caves on the North Island?\nA. Waitomo\nB. Pukeatua\nC. Tihoi\nD. Kaeo",
    "What is the name of this 328m high landmark in Auckland?\nA. Eiffel Tower\nB. Sky Tower\nC. Big Ben\nD. Tower",
    "Can you name the highest mountain in New Zealand?\nA. Mount Ruapehu\nB. Mount Tasman\nC. Mount Cook\nD. Mount Tongariro",
    "(True or False) The South Island the largest island in the world?\nA. True\nB. False",
    "What does the māori word \"Taraka\" mean?\nA. Car\nB. Airplane\nC. Bird\nD. Truck"
]
LIST_ANSWERS = [ # A list with all the answers
    "A", "B", "A", "A", "B", "C", "B", "D"
]
LIST_CHAT = [ # A list with all the other things I have to say.
    "Welcome to Kaedyn's quiz! Whats your name?",
    "Ok! Please wait three seconds and then the quiz will restart.",
    "Alright, thanks for playing!",
    "Ensure you input A, B, C, or D for your answers.",
    "Would you like to play again? (Yes or no)\nAnswer: ",
    "Yes",
    "No",
    "Please enter A, B, C, or D."
]

# Intro & Question Print Loop
print(LIST_CHAT[0])
str_name = input("Name: ") # User name input
time.sleep(0.75)
print(LIST_CHAT[3])
def playing():
    global int_score
    global str_name
    for i in range (len(LIST_QUESTIONS)):
        time.sleep(3)
        print("\n")
        print(f"{LIST_QUESTIONS[i]}\n")
        while True: # If answer isn't in LIST_VALID_ANSWERS, user must input again, if it is, it will continue.
            ans = input("Answer: ").lower().title()
            if ans in LIST_VALID_ANSWERS:
                break
            print(LIST_CHAT[7])
        if ans == LIST_ANSWERS[i]:
            int_score += 5
            print(f"✅  That's right! You now have {int_score} points.")
            i += 1
        else: 
            int_score -= 2.5
            print(f"❌  That's wrong. The answer was {LIST_ANSWERS[i]}.\nYou now have {int_score} points.")
            i += 1

def runit():
    global int_score
    time.sleep(1)
    print("\n")
    if int_score > INT_PASSING_SCORE: # Check user score
        print(f"Alright, {str_name}. You passed my quiz with {int_score} points! ") # Passed the quiz
    else:
        print(f"Nice try, {str_name}! You failed my quiz with {int_score} points\nYou need at least 20 points to pass.") # Failed the quiz

    tryagain = input(LIST_CHAT[4])
    tryagain = tryagain.lower().title()
    if tryagain == LIST_CHAT[5]:
        print(LIST_CHAT[1])
        int_question = 0
        int_score = 0
        time.sleep(3)
        os.system('clear')
        playing()
    elif tryagain == LIST_CHAT[6]:
        print(LIST_CHAT[2])
        quit()
    else:
        print(f"Hey! {str_name}! It's a yes or no question!")
        time.sleep(1)
        runit()
playing()
runit()
