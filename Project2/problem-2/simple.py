# [[0, 32, 45], [2, 5, 19], [7, 6, 25]],
# [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

# [(0, 's', [7, (0, 0)]),
# (1, 's', [2, (0, 0)]),
# (2, 's', [25, (0, 0)])]

# [2, 5, -1, 19]

# {0: [(0, 's', [7, (0, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])],
# 1: [(0, 's', [5, (1, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])],
# 2: [(0, 's', [0, (2, 0)]), (1, 's', [0, (1, 0)]), (2, 's', [25, (0, 0)])],
# 3: [(0, 's', [1, (2, 1)]), (1, 's', [0, (1, 0)]), (2, 's', [23, (1, 0)])],
# 4: [(0, 's', [1, (2, 1)]), (1, 's', [0, (1, 0)]), (2, 's', [18, (2, 0)])],
# 5: [(0, 's', [1, (2, 1)]), (1, 's', [0, (1, 0)]), (2, 's', [19, (2, 1)])],
# 6: [(0, 's', [1, (2, 1)]), (1, 's', [0, (1, 0)]), (2, 's', [0, (2, 2)])]}


def find_distance(elevations, path):
    distance = (
        elevations[x][y] - elevations[m][n]
        for (x, y), (m, n) in zip(path[1:], path)
    )
    answer = {p: d for p, d in zip(path, distance)}
    return answer


def check_id(pony, timestep):
    # check if pony id < timestep
    return pony[0] < timestep


def check_more(pony, path):
    # Get the last element of the tuple and check if it's equal to the maximum value in the path list
    return pony[-1][-1] != max(path)


def check_energy(pony, path_diff):
    return pony[-1][0] >= path_diff[pony[-1][-1]]


# def move(pony, path_diff, path):
#     location = path[path.index(pony[-1][-1]) + 1]
#     return pony[0], 's', [pony[-1][0] - path_diff[pony[-1][-1]], location]

def move(pony, path_diff, timestep, path):
    for index in range(len(path)):
        if path[index] == pony[-1][-1]:
            location = path[index + 1]
    pony_list = [pony[-1][0] > path_diff[pony[-1][-1]], location]
    return (timestep, 's', pony_list)

def selfish_climb(elevations, path, ponies):
    timestep = 0
    log = {}
    path_diff = find_distance(elevations, path)
    print(f"path_diff: {path_diff}\n")
    consider = []
    trythis(ponies, path, path_diff, log, 0)
    trythis(ponies, path, path_diff, log, 1)
    trythis(ponies, path, path_diff, log, 2)
    # trythis(ponies, path, path_diff, log, 3)
    # trythis(ponies, path, path_diff, log, 4)
    # trythis(ponies, path, path_diff, log, 5)
    # trythis(ponies, path, path_diff, log, 6)


def trythis(ponies, path, path_diff, log, timestep):
    consider = []
    pony = (0, 's', [7, (0, 0)])
    # print(f"pony[0] = {pony[0]}")
    print(f"timestep = {timestep}")
    print(check_id(pony, timestep), check_more(
        pony, path), check_energy(pony, path_diff))
    if check_id(pony, timestep) and check_more(pony, path) and check_energy(pony, path_diff):
        # print("move")
        print(f"{pony}\n{path_diff}\n{path}\n")
        one_pony = move(pony, path_diff, path)
        print(f"one_pony: {one_pony}")
        consider.append(one_pony)
    else:
        consider.append(pony)
    print(f"consider: {consider}\n")
    # print(f"log[{timestep}]: {log[timestep]}")
    if timestep in log and consider == log[timestep]:
        #         exit
        print(f"end: {consider == log[timestep]}")
        runnable = False
    else:
        log[timestep] = consider

        for key, value in log.items():
            print(f'{key}: {value}')

        print('\n')


#             check id
#             check if at the final destination
#             check energy enough
#             update list
#         make change to dict
#     timestep++
print(selfish_climb([[0, 32, 45], [2, 5, 19], [7, 6, 25]], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
                    [(0, 's', [7, (0, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])]))
