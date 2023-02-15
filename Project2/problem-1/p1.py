import ast

def read_file(file_name):
    with open(file_name, "r") as f:
        result = []
        data = f.read()
        data_separated = data.split("\n\n")

        # split data according to newline and get rid of the string header
        elevations = data_separated[0].split("\n")[1:]
        path = data_separated[1].split("\n")[1:]
        ponies = data_separated[2].split("\n")[1:]
        result.append(split_elevation(elevations))
        result.append(split_path(path))
        result.append(split_ponies(ponies))
        # print(elevations)
        # print("\n")
        # print(path)
        # print("\n")
        # print(ponies)
        # print("\n")

def split_elevation(elevations):
    # create list of lists of integers
    final_data_elevations = [[int(num) for num in item.split(", ")] for item in elevations]
    # print(final_data_elevations)
    return final_data_elevations


def split_path(paths):
    # create list of tuple of integers
    final_data_path = [eval(item) for item in paths]
    # print(final_data_path)
    return final_data_path


def parse_string(my_string):
    # Remove the square brackets from the string and split it
    my_list = my_string[1:-1].split(", ")

    # Convert the first element of the list to an integer
    my_list[0] = int(my_list[0])

    # join the [30,(0,0)] back together
    clean_tuple = ",".join(my_list[1:])

    # Remove the square brackets from the string and split it
    my_tuple = clean_tuple[1:-1].split(",")

    #turn the items into int and create the tuple
    answer_tuple = (int(my_tuple[0]),int(my_tuple[1]))

    # set the second element of the list the tuple
    my_list[1] = answer_tuple
    return my_list[:-1]


def split_ponies(ponies):
    final_data_ponies = []
    for p in ponies:
        pony_list = []
        split_p = p.split(", ")
        pony_list.append(int(split_p[0]))
        pony_list.append(split_p[1])
        last_items = ", ".join(split_p[2:])
        last_list = parse_string(last_items)
        pony_list.append(last_list)
        final_data_ponies.append(pony_list)
    return final_data_ponies



read_file("file_example1.txt")