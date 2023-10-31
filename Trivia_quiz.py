import random

# Questions and their corresponding answers in a dictionary
questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal in the world?": "Blue Whale",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the largest organ in the human body?": "Skin"
}

def get_random_question():
    question = random.choice(list(questions.keys()))
    answer = questions[question]
    return question, answer

def quiz():
    score = 0
    print("Welcome to the Trivia Quiz Game!")
    print("Answer the following questions:")
    print("Enter 'quit' at any time to exit the game.")
    print()

    while True:
        question, answer = get_random_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").capitalize()

        if user_answer == 'Quit':
            break

        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is '{answer}'.")

    print(f"Thanks for playing! Your total score is: {score}.")

if __name__ == "__main__":
    quiz()
