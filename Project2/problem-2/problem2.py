def find_distance(elevations, path):
    # Use tuple unpacking to extract the path list
    # and the elevations list of lists
    distance_list = [
        elevations[x][y] - elevations[m][n]
        for i, (x, y) in enumerate(path[1:])
        for m, n in [path[i]]
    ]
    return distance_list


def run_pony(timestep, p, distance_list,path):
    if p[0] < timestep:



def selfish_climb(elevations, path, ponies):
    if path[-1] != max(path):
        return "Path should end at {} coordinate".format(max(path))

    distance_list = find_distance(elevations, path)
    print(distance_list)
    # [2, 5, -1, 19]
    timestep = 1

    while timestep:
        log = {timestep - 1: ponies}
        # check end
        for p in ponies:
            if p[-1][-1] == max(path) or log[timestep - 1] == log[timestep - 2]:
                exit()
            else:
                run_pony(timestep, p, distance_list)

                print(log)
            timestep += 1
        if timestep == 7:
            exit()


selfish_climb([[0, 32, 45], [2, 5, 19], [7, 6, 25]], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
              [(0, 's', [7, (0, 0)]), (1, 's', [2, (0, 0)]), (2, 's', [25, (0, 0)])])
