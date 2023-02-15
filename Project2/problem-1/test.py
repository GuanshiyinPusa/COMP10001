def read_file(file_name):
    with open(file_name, "r") as f:
        data_separated = f.read().split("\n\n")
        elevations = data_separated[0].split("\n")[1:]
        path = data_separated[1].split("\n")[1:]
        ponies = data_separated[2].split("\n")[1:]
        result = (split_elevation(elevations),split_path(path),split_ponies(ponies))
        return result


def split_elevation(elevations):
    final_data_elevations = [[int(num) for num in item.split(", ")] for item in elevations]
    return final_data_elevations


def split_path(paths):
    final_data_path = [eval(item) for item in paths]
    return final_data_path


def parse_string(my_list):
    my_list[0] = int(my_list[0].strip("["))
    my_tuple = ",".join(my_list[1:]).strip("()]").split(",")
    my_list[1] = (int(my_tuple[0]),int(my_tuple[1]))
    return my_list[:-1]


def split_ponies(ponies):
    final_data_ponies = []
    for p in ponies:
        split_p = p.split(", ")
        pony_tuple = (int(split_p[0]), split_p[1],parse_string(split_p[2:]))
        final_data_ponies.append(pony_tuple)
    return final_data_ponies

print(read_file("file_example1.txt"))