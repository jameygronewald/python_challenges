number_to_check = int(input(f"What number would you like to see all divisors of?   "))

# list comprehension solution
print([ x for x in range(1, number_to_check + 1) if number_to_check % x == 0])

# filter/lambda solution
print(list(filter(lambda x: number_to_check % x == 0, range(1, number_to_check + 1))))
    