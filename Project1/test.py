pony_capacities = [17, 37, 73]
journey_path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)]
pony_assignments = [(73, 73)] * 6
village_elevations = [[100, 200, 300, 400, 100, 600], [0, 100, 200, 300, 400, 500]]


def closest_greater_or_equal_number(arr, target):
    closest_tuple = None
    min_diff = float('inf')

    for tup in arr:
        if tup[0] + tup[1] >= target:
            diff = abs(tup[0] + tup[1] - target)
            if diff < min_diff:
                min_diff = diff
                closest_tuple = tup

    if closest_tuple:
        return closest_tuple
    else:
        return None


def assign_pony_to_path(elevations, path, capacities):
    # list all the possible capacities
    possible_capacities = []
    for i in range(len(capacities)):
        for j in range(i, len(capacities)):
            possible_capacities += [(capacities[i], capacities[j])]
    print(possible_capacities)

    # find the distance between villages
    final_elevation = [elevations[x][y] for x, y in path]
    distance = [abs(final_elevation[i + 1] - final_elevation[i])
                for i in range(len(final_elevation) - 1)]
    print("distance: "
          + str(distance))

    ans_capacity = []
    for m in distance:
        ans_capacity += [closest_greater_or_equal_number(possible_capacities, m)]
    print(ans_capacity)


assign_pony_to_path(village_elevations, journey_path, pony_capacities)
