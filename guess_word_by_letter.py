word = "EVAPORATE"

list = ['_' for char in word]

guessed = []

def init():
    print()
    print(*list)

    while '_' in list:

        print('\nTry to guess the word!')
        user_guess = input('Enter a letter to guess:   ').upper().strip()

        if len(user_guess) > 1:
            print('\nPlease enter only one letter as a guess.')

        elif user_guess in guessed:
            print('\nYou already guessed that one. Try a different letter.')

        else:
            guessed.append(user_guess)
            for i in range(len(word)):
                if word[i] == user_guess:
                    list[i] = user_guess
        print()
        print(*list)
    
    print(f"\nYou got it! The word was {word}")

init()