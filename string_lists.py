string = input('Please enter in a string and I will determine whether it is a palindrome or not.   ')


print(string[0:int(len(string)/2)] == string[::-1][0:int(len(string)/2)])

# way to get last half of string, could use this and the reverse and compare
# print(string[-int(len(string)/2) : len(string)])
