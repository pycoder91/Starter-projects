import random

def hangman():
    words = ["apple", "banana", "orange", "strawberry", "pineapple", "watermelon"]  # List of words for the game
    secret_word = random.choice(words).lower()  # Choosing a random word from the list
    guessed_letters = []  # To store the guessed letters
    attempts = 6  # Total attempts allowed for guessing

    print("Welcome to Hangman!")
    print("_ " * len(secret_word))  # Displaying the initial placeholders for the word

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        else:
            print("Good guess!")

        # Displaying the word with correctly guessed letters
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Checking if the player has guessed all the letters
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You've guessed the word!")
            break

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{secret_word}'.")

if __name__ == "__main__":
    hangman()
