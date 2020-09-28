import random

def init():
    target_num = random.randint(1000, 9999)
    target_string = str(target_num)
    correct = False
    guesses = 0
    while correct is False:
        cows = 0
        bulls = 0
        user_guess = (input(f"Can you guess the 4-digit number? Enter 4 digits and hit 'enter':   "))
        if len(user_guess) != 4:
            print(f"Please enter a valid guess of 4 digits.")
        else:
            guesses += 1
            i = 0
            for i in range(4):
                if user_guess[i] == target_string[i]:
                    cows += 1
                elif user_guess[i] in target_string:
                    bulls += 1
            if cows == 4:
                print(f"You win! The 4 digit number was {target_num}. And it only took you {guesses} guesses!")
                break
            print(f"You have {cows} cows and {bulls} bulls. You've guessed {guesses} times. Try again.")

if __name__ == "__main__":
    init()