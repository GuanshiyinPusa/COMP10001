def check_move(pony, path, path_diff, timestep):
    if check_id(pony, timestep) and check_more(pony, path) and check_energy(pony, path_diff):
        for index in range(len(path)):
            if path[index] == pony[-1][-1]:
                location = path[index + 1]
        pony_list = [pony[-1][0] - path_diff[pony[-1][-1]], location]
        return (pony[0], 's', pony_list)
    return pony


def check_id(pony, timestep):
    # check if pony id < timestep
    return pony[0] < timestep


def check_more(pony, path):
    # Get the last element of the tuple and check if it's equal to the maximum value in the path list
    return pony[-1][-1] != max(path)


def check_energy(pony, path_diff):
    return pony[-1][0] >= path_diff[pony[-1][-1]]


def loop_ponies(ponies, path, path_diff, timestep):
    pony_list = []
    for pony in ponies:
        pony_list.append(check_move(pony, path, path_diff, timestep))
    return pony_list


pony_0 = (0, 's', [7, (0, 0)])
pony_1 = (0, 's', [5, (1, 0)])
pony_2 = (0, 's', [0, (2, 0)])
pony_3 = (0, 's', [1, (2, 1)])

pony_4 = (1, 's', [2, (0, 0)])
pony_5 = (1, 's', [0, (1, 0)])


path_diff = {(0, 0): 2, (1, 0): 5, (2, 0): -1, (2, 1): 19}
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

ponies_0 = [(0, 's', [7, (0, 0)]),
            (1, 's', [2, (0, 0)]),
            (2, 's', [25, (0, 0)])]

ponies_1 = [(0, 's', [5, (1, 0)]),
            (1, 's', [2, (0, 0)]),
            (2, 's', [25, (0, 0)])]

ponies_2 = [(0, 's', [0, (2, 0)]), 
            (1, 's', [0, (1, 0)]), 
            (2, 's', [25, (0, 0)])]

ponies_3 = [(0, 's', [1, (2, 1)]), 
            (1, 's', [0, (1, 0)]), 
            (2, 's', [23, (1, 0)])]

ponies_4 = [(0, 's', [1, (2, 1)]), 
            (1, 's', [0, (1, 0)]), 
            (2, 's', [18, (2, 0)])]

ponies_5 = [(0, 's', [1, (2, 1)]), 
            (1, 's', [0, (1, 0)]), 
            (2, 's', [19, (2, 1)])]
ponies_6 = [(0, 's', [1, (2, 1)]), 
            (1, 's', [0, (1, 0)]), 
            (2, 's', [0, (2, 2)])]

print(loop_ponies(ponies_6, path, path_diff, 6))
