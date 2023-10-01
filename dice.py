import random

while True:
    input("Press Enter to roll the die...")
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}")
    play_again = input("Roll again? (yes/no): ").lower()
    if play_again != "yes":
        break
