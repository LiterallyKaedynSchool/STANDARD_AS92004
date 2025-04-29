'''
STANDARD AS92004 Quiz About New Zealand
Kaedyn Eastall
Licensed with the JSS General Public License 001 - https://github.com/Jester-Software-Systems/JSS_LICENSE_DIRECTORY/blob/2025-Licenses/MARCH/JSS-GPL1
'''
import time

# Lists & Variables
int_score = 0
int_question = 0
LIST_QUESTIONS = [
    "Who found New Zealand?",
    "What is the capital of New Zealand?",
    "Where is the big carrot?",
    "What does \"Kia Ora\" mean?",
    "What is the name of the glowworm caves on the North Island?",
    "What is the name of this 328m high landmark in Auckland?",
    "Can you name the highest mountain in New Zealand?",
    "(True or False) The South Island the largest island in the world?"
]
LIST_ANSWERS = [
    "Abel Tasman",
    "Wellington",
    "Ohakune",
    "Hello",
    "Waitomo",
    "Sky Tower",
    "Mount Cook",
    "False"
]
LIST_YAP = [
    "Welcome to Kaedyn's quiz! Let's go."
]

# Main Question Asking
print(LIST_YAP[0])
for i in range (len(LIST_QUESTIONS)):
    time.sleep(1)
    print("\n")
    print(f"{LIST_QUESTIONS[i]}")
    ans = input()
    ans = ans.lower()
    ans = ans.title()
    if ans == LIST_ANSWERS[i]:
        int_score += 5
        print(f"That's right! You now have {int_score} points.")
        i =+ 1
    else:
        int_score -= 2.5
        print(f"That's wrong. The answer was {LIST_ANSWERS[i]}.\nYou now have {int_score} points.")
        i =+ 1
