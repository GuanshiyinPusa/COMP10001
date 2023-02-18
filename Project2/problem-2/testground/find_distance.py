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


# elevations = [[0, 10, 20], [0, 0, 20], [0, 0, 0]]
# path = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]

elevations = [[0, 32, 45], [2, 5, 19], [7, 6, 25]]
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

# elevations = [[0, 0], [0, 0]]
# path = [(0, 0), (1, 0), (1, 1)]

# elevations = [[100, 90, 80, 0], [30, 20, 40, 100], [31, 45, 0, 400]]
# path = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]

print(find_distance(elevations, path))