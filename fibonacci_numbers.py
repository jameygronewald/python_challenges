numbers_to_generate = int(input(f"How many numbers would you like to see?   "))

def generate_fib_nums(nums):
    if numbers_to_generate == 0:
        print([])
    elif numbers_to_generate == 1:
        print([1])
    else:
        nums = [1, 1]
        for x in range(2, numbers_to_generate):
            new_num = nums[-1] + nums[-2]
            nums += [new_num]
        print(nums)

generate_fib_nums(numbers_to_generate)