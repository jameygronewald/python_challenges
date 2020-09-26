from datetime import datetime

current_year = datetime.now().year

name = input(f"What is your name?   ")
age = int(input(f"What age will you or did you turn in the current year?   "))
print_count = int(input(f"How many times should I print the message?   "))

years_til_100 = 100 - age

year_to_print = current_year + years_til_100

print(f"Hello {name}. Since you are {age} years old, you will turn 100 years old in the year {year_to_print}.\n" * print_count)