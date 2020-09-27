import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = []
b = []

length_of_a = random.randint(20, 50)
length_of_b = random.randint(20, 50)

for x in range (length_of_a):
    a.append(random.randint(1, 100))
for x in range (length_of_b):
    b.append(random.randint(1, 100))
print(a)
print(b)
print(list(set([x for x in a if x in b])))
