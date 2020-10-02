if __name__ == "__main__":
        
    def guess_number():
        potential_nums = [num for num in range(1, 101)]

        print(f"\nThink of a number between 1 and 100 and I will guess it. It will take me no more than 7 tries.")
        input("Press enter once you have your number.")

        guesses = 1
        guessing = True

        while guessing == True:
            try:
                guess = potential_nums[len(potential_nums) // 2]
                print(f"\nIs your number {guess}?")
                warmer = int(input("\nEnter a 1 if the guess is too low; enter a 2 if the guess is too high; enter a 0 if the guess is correct:   "))

                if warmer == 0:
                    print(f"\nYour number is {guess}. And it only took me {guesses} tries :) ")
                    break

                elif warmer == 2:
                    guesses += 1
                    potential_nums = potential_nums[:len(potential_nums) // 2]

                elif warmer == 1:
                    guesses += 1
                    potential_nums = potential_nums[(len(potential_nums) // 2) + 1:]
                
                else:
                    print(f"\nInvalid input. Please enter 1, 2, or 0.")

            except ValueError:
                print(f"\nInvalid input. Please enter 1, 2, or 0.")
            except IndexError:
                print(f"\nYou lied about your number. I don't play with liars. Goodbye.")
                break
            
    guess_number()