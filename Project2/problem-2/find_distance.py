elevations_1 = [[0, 32, 45], [2, 5, 19], [7, 6, 25]]
path_1 = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]


elevations_2 = [[0, 10, 20], [0, 0, 20], [0, 0, 0]]
path_2 = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]


elevations_3 = [[0, 0], [0, 0]]
path_3 = [(0, 0), (1, 0), (1, 1)]


elevations_4 = [[100, 90, 80, 0], [30, 20, 40, 100], [31, 45, 0, 400]], 
path_4 = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)], 


def find_distance(elevations, path):
    distance = [
        elevations[x][y] - elevations[m][n]
        for i, (x, y) in enumerate(path[1:])
        for m, n in [path[i]]
    ]
    answer = {}
    for index in range(len(distance)):
        answer[path[index]] = distance[index]
    return answer

print(find_distance(elevations_1, path_1))
print(find_distance(elevations_2, path_2))
print(find_distance(elevations_3, path_3))
print(find_distance(elevations_4, path_4))