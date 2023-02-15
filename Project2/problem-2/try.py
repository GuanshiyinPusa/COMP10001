# [[0, 32, 45], [2, 5, 19], [7, 6, 25]],
# [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],

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
    # pony = (0, 's', [7, (0, 0)])
    if pony[0] < timestep:
        return True
    else:
        return False
    
def check_more(pony, path):
    # (0, 's', [7, (0, 0)])
    if pony[-1][-1] == max(path):
        return False
    else:
        return True

def check_energy(ponies, path_diff):
    return False
    

def selfish_climb(elevations, path, ponies):
    #     initialize timestep
    timestep = 0
    # initialize dict
    log = {}
    log[timestep] = ponies
    # generate the elevation difference
    path_diff = find_distance(elevations, path)
    print(path_diff)


# when (timestep + 1):
    while (timestep + 1):
#       initialize consider
        consider = []
#     if consider == the last key item
        if consider == log[timestep]:
#         exit
            return log
#         for each horse
        for pony in ponies:
            if check_id and check_more and check_energy:
                return 0
#             check id
#             check if at the final destination
#             check energy enough
#             update list
#         make change to dict
#     timestep++

selfish_climb([[0, 32, 45], [2, 5, 19], [7, 6, 25]], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
              [(0, 's', [7, (0, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])])
