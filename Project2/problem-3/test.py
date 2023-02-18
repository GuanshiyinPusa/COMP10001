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


def find_lucky(pony, log, path, distance_list):
    current_timestep = max(log, key = int)
    print(current_timestep)
    for i in range(pony[0]):
        # iterate the ponies before altruistic
        compared_pony = log[current_timestep][i]
        print(pony)
        print(compared_pony)
        # check some location
        if compared_pony[-1][-1] == pony[-1][-1]:
            print("yes1")
            # find the energy for next
            path_index = path.index(pony[-1][-1])
            # energy for next
            next_energy = distance_list[path_index]
            #check if a pony has enough energy to share
            if pony[-1][0] >= next_energy:
                print("yes2")
            # give the compared pony 
                compared_pony[-1][0] = next_energy
                print(pony[-1][0])
                print(next_energy)
                pony[-1][0] = pony[-1][0] - next_energy
                # check if pony has enough energy if yes, move one 
            return pony
    print("no")
    return False


def teamwork_climb(elevations, path, ponies):
    distance_list = find_distance(elevations, path)

    # TODO
    # initiate timestep
    timestep = 4
    # initiate the log
    # log = {0 : ponies}
    log = {0: [(0, 's', [2, (0, 0)]), (1, 's', [6, (0, 0)]), (2, 'a', [14, (0, 0)])],
           1: [(0, 's', [0, (0, 1)]), (1, 's', [6, (0, 0)]), (2, 'a', [14, (0, 0)])],
           2: [(0, 's', [0, (0, 1)]), (1, 's', [4, (0, 1)]), (2, 'a', [14, (0, 0)])],
           3: [(0, 's', [0, (0, 1)]), (1, 's', [1, (0, 2)]), (2, 'a', [12, (0, 1)])],
           4: [(0, 's', [0, (0, 1)]), (1, 's', [1, (0, 2)]), (2, 'a', [12, (0, 1)])]}

    # check id

    # for timestep fixed
    for pony in ponies:
        if pony[0] < timestep:
            # check if altruistic
            if pony[1] == 'a':
                
                # check if there is any pony at the same location
                find_lucky(pony, log, path, distance_list)
    return log

print(teamwork_climb([[0, 2, 5], [0, 0, 10]], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 's', [2, (0, 0)]), (1, 's', [6, (0, 0)]), (2, 'a', [14, (0, 0)])]))