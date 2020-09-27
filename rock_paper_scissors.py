import random

def init():
    user_choice = input(f"Rock, paper, scissors, SHOOT!\n(Select 'r', 'p', or 's' on your keyboard.)   ")
    potential_computer_responses = ['r', 'p', 's']
    computer_choice = random.choice(potential_computer_responses)
    print(f"\nYou choose {user_choice} and computer chooses {computer_choice}...   \n")
    if user_choice == computer_choice:
        play_again = input(f"It's a draw! Play again?\n(y/n)   ")
    elif user_choice == 'r' and computer_choice == 's' or user_choice == 'p' and computer_choice == 'r' or user_choice == 's' and computer_choice == 'p':
        play_again = input(f"You win! Play again?\n(y/n)   ")
    else:
        play_again = input(f"You lose... :( Play again?\n(y/n)   ")
    if play_again == 'y':
            init()

init()