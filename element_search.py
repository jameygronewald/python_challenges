import random

if __name__ == "__main__":
        
    test_scores = []

    for _ in range(1000000):
        test_scores.append(random.randint(0, 100000))

    test_scores.sort()

    def binary_search(num, searched_list):
        in_list = False
        iterations = 0
        while len(searched_list) > 1 and in_list is False:
            iterations += 1
            index_to_test = len(searched_list) // 2
            if searched_list[index_to_test] == num:
                in_list = True
                return print(in_list, iterations)
            elif searched_list[index_to_test] > num:
                searched_list = searched_list[:index_to_test]
            else:
                searched_list = searched_list[index_to_test:]
        return print(in_list, iterations)
            
    binary_search(9751, test_scores)

    def search_list(num, list):
        in_list = False
        iterations = 0
        for index in list:
            iterations += 1
            if num == index:
                in_list = True
                break
        return print(in_list, iterations)
    
    search_list(9751, test_scores)