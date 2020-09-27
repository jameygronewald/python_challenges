number_to_check = int(input(f"\nPlease enter a number and I will determine if it is prime or not:   "))

divisors = [ x for x in range(1, number_to_check + 1) if number_to_check % x == 0]

if len(divisors) == 2:
    print(f"\nThat's a prime number!")
else:
    print(f"\nThat's not prime, sorry.")
