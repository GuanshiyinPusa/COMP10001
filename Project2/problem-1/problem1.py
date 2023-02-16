  
def read_file_1(file_name): # shortest
    with open(file_name, "r") as f:
        content = [line.strip() for line in f.read().split("\n\n")]
    return split_elevation(content[0].split("\n")[1:]), split_path(content[1].split("\n")[1:]), split_ponies(content[2].split("\n")[1:])


def split_elevation(elevations):
    return [[int(num) for num in item.split(",")] for item in elevations]


def split_path(paths):
    return [eval(item) for item in paths]


def parse_string(my_list):
    x, y, z = [int(crap.strip(" []()")) for crap in my_list]
    return [x, (y, z)]



def split_ponies(ponies):
    final_data_ponies = []
    for p in ponies:
        split_p = p.split(",")
        pony_tuple = (int(split_p[0]), split_p[1], parse_string(split_p[2:]))
        final_data_ponies.append(pony_tuple)
    return final_data_ponies


# read_file_1("file_example1.txt")
# read_file_2("file_example2.txt")

# print(read_file_1("file_example1.txt"))
# print(read_file_1("file_example2.txt"))


# def parse_string(my_list):
#     my_list[0] = int(my_list[0].strip("["))
#     my_tuple = ",".join(my_list[1:]).strip("()]").split(",")
#     my_list[1] = (int(my_tuple[0]), int(my_tuple[1]))
#     return my_list[:-1]


# def parse_string_1(my_list): # prototype
#     clean_list = []
#     for crap in my_list:
#         clean_list.append(int(crap.strip("[]()")))
#     my_list = [clean_list[0],(clean_list[1],clean_list[2])]
#     return my_list

# def read_file_2(file_name): # best performance
#     with open(file_name, "r") as f:
#         content = f.read()
#     elevations = content.split("\n\n")[0].split("\n")[1:]
#     path = content.split("\n\n")[1].split("\n")[1:]
#     ponies = content.split("\n\n")[2].split("\n")[1:]
#     return split_elevation(elevations), split_path(path), split_ponies(ponies)

# def read_file(file_name): # prototype
#     with open(file_name, "r") as f:
#         data_separated = f.read().replace(" ", "").split("\n\n")
#         elevations = data_separated[0].split("\n")[1:]
#         path = data_separated[1].split("\n")[1:]
#         ponies = data_separated[2].split("\n")[1:]
#         return split_elevation(elevations), split_path(path), split_ponies(ponies)
  