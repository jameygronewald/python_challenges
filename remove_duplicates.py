names = ["Michele", "Robin", "Sara", "Michele"]
nums = [2, 2, 4, 5, 6, 12, 54, 54, 23, 4, 6, 54, 2, 1]

def remove_duplicates_one(list_to_edit):
    new_list = []
    i=1
    for i in range(len(list_to_edit)):
        if list_to_edit[i] in new_list:
            continue
        else:
            new_list.append(list_to_edit[i])
    print(new_list)

def remove_duplicates_two(list_to_edit):
    print(list(set(list_to_edit)))

remove_duplicates_one(nums)
remove_duplicates_two(nums)
