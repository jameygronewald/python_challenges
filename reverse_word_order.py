def reverse_word_order():
    string = input(f"Type a message with multiple words and I will reverse the word order for you.   ")
    print(" ".join(string.split()[::-1]))

reverse_word_order()