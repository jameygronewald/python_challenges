friend_birthdays = {
    "Mary Olsen": "May 8th",
    "Kerry Gronewald": "March 26th",
    "Sylvie McDaniel": "July 23rd",
    "Noah Johnson": "May 20th",
    "Ray Olsen": "July 30th",
    "Hayes Johnson": "March 13th",
    "James McDaniel": "April 20th"
}

def print_names():
    for name in friend_birthdays:
        print(name)

def ask_user():
    print(f"Hello. I know the birthday of these people:")
    print_names()
    chosen_name = input(f"Whose birthday would you like to know?   ")
    if chosen_name not in friend_birthdays:
        ask_user()
    return chosen_name

def print_birthday(person):
    for name in friend_birthdays:
        if person.lower() == name.lower():
            print(f"{person}'s birthday is {friend_birthdays[name]}")

if __name__ == "__main__":
    person = ask_user()
    print_birthday(person)
