# We are neither provided with a path nor ponies’ assignment
# pony_capacities = [17, 37, 73]
# village_elevations = [[100, 200, 300, 400, 100, 600], [0, 100, 200, 300, 400, 500]]

# given 2, find other 2 using greedy algo, then check with Question-1 function

# find_path_greedy(elevations, capacities):

import time

start_time = time.time()

pony_capacities = [17, 37, 73]
village_elevations = [[100, 200, 300, 400, 100, 600], [0, 100, 200, 300, 400, 500]]
lower_village_elevations = [[10, 20, 30, 40, 10, 60], [0, 10, 20, 30, 40, 50]]


def pick_next(a, b, max_a, max_b, elevation, answer_path):
    if a == max_a and b == max_b:
        return answer_path
    right_distance = float('inf') if a >= max_a else abs(elevation[a + 1][b] - elevation[a][b])
    up_distance = float('inf') if b >= max_b else abs(elevation[a][b + 1] - elevation[a][b])
    if right_distance >= up_distance:
        answer_path.append((a, b + 1))
        return pick_next(a, b + 1, max_a, max_b, elevation, answer_path)
    else:
        answer_path.append((a + 1, b))
        return pick_next(a + 1, b, max_a, max_b, elevation, answer_path)


def closest_greater_or_equal_number(arr, target):
    closest_tuple = None
    min_diff = None
    for tup in arr:
        if tup[0] + tup[1] < target:
            continue
        diff = abs(tup[0] + tup[1] - target)
        if not closest_tuple or diff < min_diff:
            min_diff = diff
            closest_tuple = tup
    return closest_tuple

def check_path(elevations, path, capacities, assignments):
    # Cell coordinate is out of bounds:

    for h in path:
        if h[0] > (len(village_elevations) - 1) or h[1] > (len(village_elevations[0]) - 1):
            return (path[-1], 'Cell coordinate is out of bounds')

    # Path should start at (0,0) coordinate:
    if path[0] != (0, 0):
        return (path[0], 'Path should start at (0,0) coordinate')

    # Path should end at (M,N) coordinate:
    if path[-1] != max(path):
        return f"Path should end at {max(path)} coordinate"

    # Illegal move
    for i in range(len(path) - 1):
        if path[i][0] > path[i + 1][0] or path[i][1] > path[i + 1][1]:
            return (path[i], 'Illegal move')

    # Insufficient capacity assignment
    final_elevation = [elevations[x][y] for x, y in path]
    distance = [(final_elevation[i + 1] - final_elevation[i])
                for i in range(len(final_elevation) - 1)]
    total_capacity = [sum(k) for k in assignments]

    for l in range(len(total_capacity)):
        if total_capacity[l] < distance[l]:
            return (path[l], 'Insufficient capacity assignment')

    return next(
        ((m, 'Exceeding pony limit') for m in assignments if len(m) != 2), None
    )

def assign_pony_to_path(elevations, assign_path, capacities):
    final_elevation = [elevations[x][y] for x, y in assign_path]
    distance = [(final_elevation[i + 1] - final_elevation[i])
                for i in range(len(final_elevation) - 1)]
    ans_capacity = []
    for m in distance:
        possible_capacities = [(capacities[i], capacities[j]) for i in range(len(capacities)) for j in
                               range(i, len(capacities))]
        ans_capacity.append(closest_greater_or_equal_number(possible_capacities, m))
    return ans_capacity


def find_path_greedy(elevations, capacities):
    width = len(elevations) - 1
    length = len(elevations[0]) - 1
    origin_path = [(0, 0)]
    ans_path = pick_next(0, 0, width, length, elevations, origin_path)
    ans_assignment = assign_pony_to_path(elevations, ans_path, capacities)
    if not check_path(elevations, ans_path, capacities, ans_assignment):
        return ans_path, ans_assignment



path, assignment = find_path_greedy(village_elevations, pony_capacities)
print(path)
print(assignment)
print("Program running time:", time.time() - start_time, "seconds")