names = ["Michele", "Robin", "Sara", "Michele"]
nums = [2, 2, 4, 5, 6, 12, 54, 54, 23, 4, 6, 54, 2, 1]

def remove_duplicates_one(list_to_edit):
    new_list = []
    for i in list_to_edit:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

def remove_duplicates_two(list_to_edit):
    print(list(set(list_to_edit)))

remove_duplicates_one(nums)
remove_duplicates_two(nums)
