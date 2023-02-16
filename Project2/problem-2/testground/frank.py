def find_distance(elevations, path):
    result = {}
    prev_coord = path[0]
    for coord in path[1:]:
        try:
            elevation_diff = elevations[coord[0]][coord[1]] - elevations[prev_coord[0]][prev_coord[1]]
        except IndexError:
            print(f"Removing {coord} due to IndexError")
            continue
        result[prev_coord] = elevation_diff
        prev_coord = coord
    return result


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
    return [check_move(pony, path, path_diff, timestep) for pony in ponies]


def selfish_climb(elevations, path, ponies):
    path_diff = find_distance(elevations, path)
    log = {0 : ponies}
    timestep = 0
    while True:
        log[timestep+1] = loop_ponies(log[timestep], path, path_diff, timestep+1)
        # check if reaches the final step
        if log[timestep + 1] == log[timestep] and timestep > max(
            pony[0] for pony in ponies
        ):
            del log[timestep+1]
            return log
        timestep+=1

# print(selfish_climb([[0, 32, 45], [2, 5, 19], [7, 6, 25]], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 's', [7, (0, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])]))
# print(selfish_climb([[0, 10, 20], [0, 0, 20], [0, 0, 0]], [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)], [(0, 's', [0, (0, 0)]), (1, 's', [0, (0, 0)])]))
# print(selfish_climb([[0, 0], [0, 0]], [(0, 0), (1, 0), (1, 1)], [(0, 's', [0, (0, 0)])]))
# print(selfish_climb([[100, 90, 80, 0], [30, 20, 40, 100], [31, 45, 0, 400]], [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)], [(0, 's', [0, (0, 0)]), (1, 's', [10, (0, 0)])]))