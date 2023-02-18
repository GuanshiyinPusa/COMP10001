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


elevations = [[0, 2, 5], [0, 0, 10]]

path = [(0, 0), (0, 1), (0, 2), (1, 2)]

print(find_distance(elevations, path))