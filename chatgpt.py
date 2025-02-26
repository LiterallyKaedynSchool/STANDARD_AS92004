# This is a quiz ChatGPT wrote once I asked it to make Python code and make it match the requirements of this standard.
import random

# Constants
PASSING_SCORE = 3  # Minimum score needed to pass a level

# Dictionary containing 5 levels of questions
quiz_levels = {
    1: [
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the capital of New Zealand?", "answer": "Wellington"},
        {"question": "How many legs does a spider have?", "answer": "8"},
        {"question": "What color is the sky on a clear day?", "answer": "Blue"},
        {"question": "What is 5 + 3?", "answer": "8"},
    ],
    2: [
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
        {"question": "Which ocean is the largest on Earth?", "answer": "Pacific"},
        {"question": "What is the chemical symbol for Gold?", "answer": "Au"},
        {"question": "What year did World War II end?", "answer": "1945"},
        {"question": "What is the square root of 64?", "answer": "8"},
    ],
    3: [
        {"question": "What is the capital of Japan?", "answer": "Tokyo"},
        {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
        {"question": "How many continents are there on Earth?", "answer": "7"},
        {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
    ],
    4: [
        {"question": "What is the longest river in the world?", "answer": "Nile"},
        {"question": "What is the largest planet in the Solar System?", "answer": "Jupiter"},
        {"question": "In what year did the Titanic sink?", "answer": "1912"},
        {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
        {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    ],
    5: [
        {"question": "What element has the atomic number 1?", "answer": "Hydrogen"},
        {"question": "What is the rarest blood type?", "answer": "AB negative"},
        {"question": "What country has won the most FIFA World Cups?", "answer": "Brazil"},
        {"question": "What is the speed of light in km/s?", "answer": "299792"},
        {"question": "What year did humans first land on the moon?", "answer": "1969"},
    ]
}

def ask_question(question_data):
    """Function to ask a question and check the answer."""
    user_answer = input(question_data["question"] + " ").strip()
    return user_answer.lower() == question_data["answer"].lower()

def run_quiz(level):
    """Runs the quiz for a specific level."""
    print(f"\n🔹 Level {level}: Answer the following questions.\n")
    random.shuffle(quiz_levels[level])  # Randomize questions for variety

    score = 0  # Track player's score

    for question in quiz_levels[level]:
        if ask_question(question):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {question['answer']}")

    print(f"\n🏆 Your final score for Level {level} is {score}/5.")

    if score >= PASSING_SCORE:
        print(f"🎉 Congratulations! You passed Level {level}.\n")
        return True  # Player passed
    else:
        print(f"😢 You did not pass Level {level}. Try again.\n")
        return False  # Player failed

def play_game():
    """Main game function that progresses through 5 levels."""
    current_level = 1

    while current_level <= 5:
        passed = run_quiz(current_level)

        if passed:
            if current_level == 5:
                print("🏆🎉 Congratulations! You have completed all levels! 🎉🏆")
                break
            else:
                next_step = input("Do you want to proceed to the next level? (yes/no): ").strip().lower()
                if next_step == "yes":
                    current_level += 1
                else:
                    print("Thanks for playing! Goodbye.")
                    break
        else:
            retry = input("Do you want to retry this level? (yes/no): ").strip().lower()
            if retry != "yes":
                print("Thanks for playing! Goodbye.")
                break

# Start the game
play_game()
