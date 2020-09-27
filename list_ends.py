a = [5, 10, 15, 20, 25, 45]

def get_list_extremes(list):
    print( [ x for x in list if x is list[0] or x is list[len(list) - 1]] )

get_list_extremes(a)