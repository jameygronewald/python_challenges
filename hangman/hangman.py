import sys
import random
from word_list import words


def play_again():
    print(f"\nPlay again?")
    try:
        another_game = input(f"\n(y / n)   ")
        if another_game.lower() == 'y':
            init()
        if another_game.lower() == 'n':
            print(f"\nGood game!")
            sys.exit()
        else:
            print("\nInvalid input. Please enter 'y' to play again or 'n' to quit.   ")
            play_again()
    except TypeError:
        print("\nInvalid input. Please enter 'y' to play again or 'n' to quit.   ")
        play_again()

def init():
    chosen_word = random.choice(words).strip()

    list = ['_' for char in chosen_word]

    guessed = set()

    print()
    print(*list)

    guesses = 6

    while '_' in list:

        print('\nTry to guess the word!')
        user_guess = input('Enter a letter to guess:   ').upper().strip()

        print(f"-----------------------------")

        if len(user_guess) > 1:
            print('\nPlease enter only one letter as a guess.')

        elif user_guess in guessed:
            print('\nYou already guessed that one. Try a different letter.')

        else:
            guessed.add(user_guess)
            for i in range(len(chosen_word)):
                if chosen_word[i] == user_guess:
                    list[i] = user_guess
            if user_guess not in chosen_word:
                guesses -= 1
        print(f"\nYou have {guesses} guesses remaining.")
        print(f"\nLetters that you've already guessed: {guessed}")
        print(*list)

        if guesses == 0:
            print(f"\nYou ran out of guesses. The word was {chosen_word}.")
            play_again()            
    
    print(f"\nYou got it! The word was {chosen_word}")
    play_again()

init()