import os

# print(os.path.exists('hangman/sowpods.txt'))

with open('hangman/sowpods.txt') as f:
    words = tuple(f)