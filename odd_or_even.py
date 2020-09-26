dividend = int(input(f"Choose a number to divide:   "))
divisor = int(input(f"Choose a number to divide that number by:   "))

if dividend < divisor:
    print(f"{divisor} does not divide into {dividend} evenly. The dividend should be larger than or equal to the divisor.")
else: 
    remainder = dividend % divisor
    if remainder == 0:
        print(f"{divisor} divides into {dividend} evenly.")
    else:
        print(f"{divisor} does not divide into {dividend} evenly. There is a remainder of {remainder}.")