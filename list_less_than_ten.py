a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# list comprehension solution
print([ x for x in a if x < 10 ])

# lambda/filter solution
print(list(filter(lambda x: (x < 10), a)))