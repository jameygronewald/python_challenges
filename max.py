if __name__ == "__main__":
    
    def find_max(*nums):
        largest = None
        # num_list = [num for num in nums]
        # for num in num_list:
        for num in nums:
            if largest is None:
                largest = num
            elif largest < num:
                largest = num
        print(largest)

    find_max(1, 2, 3)
    find_max(1, 2, -3)
    find_max(1, 2, -3, 14.5)