import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        attempts_remaining = max_attempts - attempts
        print(f"You have {attempts_remaining} attempts remaining.")
        guess = input("Guess a number between 1 and 20: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number}!")
            break

        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
