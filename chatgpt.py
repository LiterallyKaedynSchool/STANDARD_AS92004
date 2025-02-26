# This is a quiz ChatGPT wrote once I asked it to make Python code and make it match the requirements of this standard.
import random

# List of quiz questions stored in a collection (list of dictionaries)
quiz_questions = [
    {"question": "What is the capital of New Zealand?", "answer": "Wellington"},
    {"question": "How many legs does a spider have?", "answer": "8"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific"},
]

# Constants for minimum score requirement
PASSING_SCORE = 3

def ask_question(question_data):
    """Function to ask a question and check the answer."""
    user_answer = input(question_data["question"] + " ").strip()
    return user_answer.lower() == question_data["answer"].lower()

def run_quiz():
    """Function to run the quiz game."""
    print("\nWelcome to the Quiz Game!")
    print("Answer the questions correctly to pass.\n")

    # Shuffle questions to make it more dynamic
    random.shuffle(quiz_questions)

    score = 0  # Integer variable to store the score

    for question in quiz_questions:
        if ask_question(question):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {question['answer']}")

    print(f"\nYour final score is {score}/{len(quiz_questions)}.")

    # Selection control structure to check if the user passes
    if score >= PASSING_SCORE:
        print("🎉 Congratulations! You passed the quiz.")
    else:
        print("😢 Better luck next time.")

# Loop to allow replaying the quiz (iteration control structure)
while True:
    run_quiz()
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("Thanks for playing! Goodbye.")
        break
