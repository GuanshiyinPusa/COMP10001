def find_distance(elevations, path):
    ele_diff = []
    for i in range(1, len(path)):
        x, y = path[i]
        m, n = path[i-1]
        try:
            diff = elevations[x][y] - elevations[m][n]
        except IndexError:
            print(f"Removing {x,y} due to IndexError")
            continue
        ele_diff.append(diff)
    return ele_diff


def move_pony(pony, path, distance_list, log_value):
    # print(f"pony:\n{pony}\n\n")
    path_index = path.index(pony[-1][-1])
    next_energy = distance_list[path_index]
    # print(next_energy)
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
    # print(f"change to{pony}")
    return pony


def do_pony(ponies, timestep, path, distance_list, log_value, log):
    log_value = []
    for pony in ponies:
            if pony[0] < timestep and pony[-1][-1] != path[-1]:
                moved_pony = move_pony(pony, path, distance_list, log_value)
                log_value.append(moved_pony)
            else:
                log_value.append(pony)
        # print(timestep, log_value)
    log[timestep + 1] = log_value

def teamwork_climb(elevations, path, ponies):
    distance_list = find_distance(elevations, path)
    timestep = 0
    log = {timestep : ponies}
    # print(log)
    while True:
        log_value = []
        # print(f"timestep: {timestep}\n\n")
        for pony in ponies:
            if pony[0] < timestep and pony[-1][-1] != path[-1]:
                moved_pony = move_pony(pony, path, distance_list, log_value)
                log_value.append(moved_pony)
            else:
                log_value.append(pony)
        # print(timestep, log_value)
        log[timestep + 1] = log_value
        # check if reaches the final step
        if log[timestep + 1] == log[timestep] and timestep > max(
            pony[0] for pony in ponies
        ):
            print(f"same: {timestep + 1} same as {timestep}")
            del log[timestep+1]
            return log
        timestep+=1

teamwork_climb([[0, 32, 45], [2, 5, 19], [7, 6, 25]], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 's', [7, (0, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])])