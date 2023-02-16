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
    # check if pony id < timestep
        return pony[0] < timestep
    
def check_more(pony, path):
    # Get the last element of the tuple and check if it's equal to the maximum value in the path list
    return pony[-1][-1] != max(path)

def check_energy(pony, path_diff):
    return pony[-1][0] > path_diff[pony[-1][-1]]
    

def move(pony, path_diff, path):
    location = path[path.index(pony[-1][-1]) + 1]
    return pony[0], 's', [pony[-1][0] - path_diff[pony[-1][-1]], location]


def selfish_climb(elevations, path, ponies):
    #     initialize timestep
    timestep = 0
    # initialize dict
    log = {}
    # generate the elevation difference
    path_diff = find_distance(elevations, path)
    # print(path_diff)
    consider = []
    log[timestep] = ponies
# when (timestep + 1):
    while True:
#       initialize consider
        
#     if consider == the last key item
        
            # put it in log
            
#         for each horse
        for pony in ponies:
            print(pony)
            print(check_id(pony, timestep),check_more(pony, path),check_energy(pony, path_diff))
            if check_id(pony, timestep) and check_more(pony, path) and check_energy(pony, path_diff):
                # TODO make it happen
                # move single pony
                print("move")
                one_pony = move(pony, path_diff, path)
                print(f"one_pony: {one_pony}")
                consider.append(one_pony)
            else:
                consider.append(pony)
        print(f"consider: {consider}")
        if consider == log[timestep]:
#         exit
            print("end")
            return log
        timestep += 1
        log[timestep] = consider
        
        
#             check id
#             check if at the final destination
#             check energy enough
#             update list
#         make change to dict
#     timestep++

print(selfish_climb([[0, 32, 45], [2, 5, 19], [7, 6, 25]], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
              [(0, 's', [7, (0, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])]))
