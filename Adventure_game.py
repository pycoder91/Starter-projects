import time
import random

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("You find yourself on a mysterious, deserted island.")
    print_pause("To your left, you see a dense jungle.")
    print_pause("To your right, there's an old abandoned temple.")
    print_pause("In front of you, a winding path leads to a hidden cave.")
    print_pause("Where would you like to go first?")

def jungle(items):
    print_pause("You enter the dense jungle.")
    print_pause("You stumble upon a hidden clearing with a mystical flower.")
    if "Mystical Flower" in items:
        print_pause("You've already picked the mystical flower.")
    else:
        print_pause("You decide to take the mystical flower with you.")
        items.append("Mystical Flower")
    print_pause("You leave the jungle.")
    choose_action(items)

def temple(items):
    print_pause("You cautiously approach the ancient temple.")
    print_pause("There are mysterious symbols on the walls.")
    print_pause("You find an ancient artifact.")
    if "Ancient Artifact" in items:
        print_pause("There's nothing else to find here.")
    else:
        print_pause("You decide to take the ancient artifact with you.")
        items.append("Ancient Artifact")
    print_pause("You leave the temple.")
    choose_action(items)

def cave(items):
    print_pause("You venture into the hidden cave.")
    print_pause("It's dark and damp.")
    print_pause("You find a treasure chest!")
    if "Treasure" in items:
        print_pause("You've already found the treasure.")
    else:
        print_pause("You decide to open the treasure chest.")
        print_pause("Congratulations! You found the treasure.")
        items.append("Treasure")
    print_pause("You leave the cave.")
    choose_action(items)

def ending(items):
    print_pause("You have explored the island thoroughly.")
    print_pause("You possess the mystical flower, ancient artifact, and the treasure.")
    print_pause("You leave the island, enriched with discoveries and win the game!")

def choose_action(items):
    print_pause("Where would you like to go now?")
    choice = input("Enter 1 for the jungle, 2 for the temple, 3 for the cave: ")
    if choice == "1":
        jungle(items)
    elif choice == "2":
        temple(items)
    elif choice == "3":
        cave(items)
    else:
        choose_action(items)

def play_game():
    items = []
    intro()
    choose_action(items)
    ending(items)

if __name__ == "__main__":
    play_game()
