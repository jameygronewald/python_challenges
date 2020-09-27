import random

random_num = random.randint(1, 9)
attempts = 1
guess_is_correct = False
while guess_is_correct == False:
    try:
        user_guess_string = input(f"Try to guess the random number from 1-9. Type your response and hit enter or respond with 'exit' to quit the game.   ")
        if user_guess_string == "exit":
            break
        user_guess = int(user_guess_string)
        if user_guess in range(1, 10):
            if user_guess == random_num:
                print(f"You guessed it in {attempts} attempts! Good job.")
                guess_is_correct = True
            elif user_guess > random_num:
                print(f"Your guess is too high. That was attempt number {attempts}. Try again.")
                attempts += 1
            else:
                print(f"Your guess is too low. That was attempt number {attempts}. Try again.")
                attempts += 1
        else:
            print('Please enter a valid integer guess.')
    except ValueError:
        print('Please enter a valid integer guess.')