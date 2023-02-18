def move_pony(pony, path, distance_list, log_value):
    path_index = path.index(pony[-1][-1])
    next_energy = distance_list[path_index]
    print(next_energy)
    if pony[1] == "a":
        for before in range(pony[0]):
            before_pony = log_value[before]
            if before_pony[-1][-1] == pony[-1][-1]:
                if pony[-1][0] >= next_energy:
                    before_pony[-1][0] = next_energy
                    pony[-1][0] = pony[-1][0] - next_energy
    if pony[-1][0] >= next_energy:
        next_step = path_index + 1
        pony[-1][0] = pony[-1][0] - next_energy
        pony[-1][-1] = path[next_step]
    print(pony)
    return pony


pony = (2, 's', [23, (1, 0)])
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
distance_list = [2, 5, -1, 19]
log_value = []
move_pony(pony, path, distance_list, log_value)
