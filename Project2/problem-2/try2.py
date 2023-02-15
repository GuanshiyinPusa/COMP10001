def find_distance(elevations, path):
    distance = (
        elevations[x][y] - elevations[m][n]
        for (x, y), (m, n) in zip(path[1:], path)
    )
    answer = {p: d for p, d in zip(path, distance)}
    return answer



elevations = [[0, 32, 45], [2, 5, 19], [7, 6, 25]]
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

print(find_distance(elevations, path))