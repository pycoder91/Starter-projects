import random

def hangman():
    words = ['python', 'hangman', 'coding', 'game', 'player', 'guess', 'word', 'computer']
    secret_word = random.choice(words)
    word_length = len(secret_word)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(f"The word contains {word_length} letters.")
    print("You have 6 attempts to guess the word.")

    while attempts > 0:
        display = ''
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + ' '
            else:
                display += '_ '

        print(display)

        if '_' not in display:
            print("Congratulations! You've guessed the word.")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. Attempts left: {attempts}")
        else:
            print("Good guess!")

    if '_' in display:
        print(f"Sorry, you've run out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
