import re
import os

print (os.path.exists("read_from_file/names.txt"))

if __name__ == "__main__":

    name_dict = {}

    with open('read_from_file/names.txt') as name_file:
        line = name_file.readline()
        while line:
            line = line.strip()
            if line in name_dict:
                name_dict[line] += 1
            else:
                name_dict[line] = 1
            line = name_file.readline()
    
    print(name_dict)

    category_dict = {}

    with open("read_from_file/sun.txt") as sun_file:
        line = sun_file.readline()
        while line:
            line = line[3: -25]
            line = line.strip('/')
            if line in category_dict:
                category_dict[line] += 1
            else:
                category_dict[line] = 1
            line = sun_file.readline()
        print(category_dict)
        

    