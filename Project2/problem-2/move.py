def move(pony, path_diff, path):
    for index in range(len(path)):
        if path[index] == pony[-1][-1]:
            location = path[index + 1]
    pony_list = [pony[-1][0] - path_diff[pony[-1][-1]], location]
    return (pony[0], 's', pony_list)

pony_0 = (0, 's', [7, (0, 0)])
pony_1 = (0, 's', [5, (1, 0)])
pony_2 = (0, 's', [0, (2, 0)])
pony_3 = (0, 's', [1, (2, 1)])

pony_4 = (1, 's', [2, (0, 0)])
pony_5 = (1, 's', [0, (1, 0)])


path_diff = {(0, 0): 2, (1, 0): 5, (2, 0): -1, (2, 1): 19}
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

print(move(pony_0, path_diff, path))
print(move(pony_1, path_diff, path))
print(move(pony_2, path_diff, path))
# print(move(pony_4, path_diff, path))
