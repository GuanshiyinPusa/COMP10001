# [(0, 's', [7, (0, 0)]),
# (1, 's', [2, (0, 0)]),
# (2, 's', [25, (0, 0)])]

pony = (0, 's', [7, (0, 0)])
path_diff = {(0, 0): 2, (1, 0): 5, (2, 0): -1, (2, 1): 19}

# [2, 5, -1, 19]
def check_energy(pony, path_diff):
    return pony[-1][0] > path_diff[pony[-1][-1]]

print(check_energy(pony, path_diff))