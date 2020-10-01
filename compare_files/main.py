if __name__ == "__main__":

    def get_list_from_file(filename):
        int_list = []
        with open(f"compare_files/{filename}") as f:
            line = f.readline()
            while line:
                int_list.append(int(line))
                line = f.readline()
        return int_list

    prime_list = get_list_from_file('one.txt')
    happy_list = get_list_from_file('two.txt')

    common_list = [num for num in prime_list if num in happy_list]

    print(common_list)