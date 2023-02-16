pony = (2, 's', [25, (0, 0)])
path_diff = {(0, 0): 2, (1, 0): 5, (2, 0): -1, (2, 1): 19}
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
timestep = 0


def move(pony, path_diff, path):
    location = path[path.index(pony[-1][-1]) + 1]
    return pony[0], 's', [pony[-1][0] - path_diff[pony[-1][-1]], location]

print(move(pony, path_diff, path))

