# The function returns None if the assigned ponies are capable of getting from the initial
# (0,0) point to the destination using the provided path. Otherwise, it should a tuple with a
# cell coordinate* and associated error message string.

# =================================================================================================================== #
# Error Catch:

# Cell coordinate is out of bounds:
# A cell listed in path is out of map boundaries according to cell_elevations Overflow error

# Path should start at (0,0) coordinate:
# The first element of the path is not (0,0)

# Path should end at (M,N) coordinate:
# The path last element isn't the cell (village) with maximum coordinates, as found from village_elevations
# (replace M,N with particular values for the current data)

# Illegal move
# The path contains any move other than plus one x coordinate or plus one y coordinate.(*)

# Insufficient capacity assignment
# Assigned pony capacity isn't enough to overcome an elevation raise on the way to the next cell in path. (*)

# Exceeding pony limit
# A pony assignment for a move contains more than two ponies (*)

# =================================================================================================================== #


def check_path(elevations, path, capacities, assignments):
    # Cell coordinate is out of bounds:

    for h in path:
        if h[0] > (len(village_elevations) - 1) or h[1] > \
                (len(village_elevations[0]) - 1):
            return path[-1], 'Cell coordinate is out of bounds'

    # Path should start at (0,0) coordinate:
    if path[0] != (0, 0):
        return path[0], 'Path should start at (0,0) coordinate'

    # Path should end at (M,N) coordinate:
    if path[-1] != max(path):
        return f"Path should end at {max(path)} coordinate"

    # Illegal move
    for i in range(len(path) - 1):
        if path[i][0] > path[i + 1][0] or path[i][1] > path[i + 1][1]:
            return path[i], 'Illegal move'

    # Insufficient capacity assignment
    final_elevation = [elevations[x][y] for x, y in path]
    distance = [(final_elevation[i + 1] - final_elevation[i])
                for i in range(len(final_elevation) - 1)]
    total_capacity = [sum(k) for k in assignments]

    for l in range(len(total_capacity)):
        if total_capacity[l] < distance[l]:
            return path[l], 'Insufficient capacity assignment'

    return next(
        ((m, 'Exceeding pony limit') for m in assignments if len(m) != 2), None
    )


pony_capacities = [17, 37, 73]
journey_path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)]
pony_assignments = [(73, 73)] * 6
village_elevations = [[100, 200, 300, 400, 100, 600],
                      [0, 100, 200, 300, 400, 500]]

journey_path_1 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 6)]

journey_path_2 = [(0, 1), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)]

pony_assignments_3 = [(73, 17)] * 6


def main():
    print(check_path(village_elevations, journey_path, pony_capacities, pony_assignments))
    print("\n")
    print(check_path(village_elevations, journey_path_1, pony_capacities, pony_assignments))
    print("\n")
    print(check_path(village_elevations, journey_path_2, pony_capacities, pony_assignments))
    print("\n")
    print(check_path(village_elevations, journey_path, pony_capacities, pony_assignments_3))
    print("\n")


if __name__ == "__main__":
    main()

# The code defines a function check_path() which takes four arguments: elevations, path, capacities, and assignments.

# The function checks if the given path is valid according to certain rules.
# If the path is invalid, it prints an error message with the invalid cell coordinate and the reason why it is invalid.
# If the path is valid, it prints "None" and returns 0.

# The function checks for the following conditions:

# If the cell coordinate is out of bounds, it prints "Cell coordinate is out of bounds" and returns 0.
# If the path does not start at the (0,0) coordinate, it prints "Path should start at (0,0) coordinate" and returns 0.
# If the path does not end at the (M,N) coordinate, it prints "Path should end at (M,N) coordinate" and returns 0.
# If the path contains any illegal moves (i.e. moving in a direction that is not to the right or down),
# it prints "Illegal move" and returns 0.
# If the capacity assignments are insufficient, it prints "Insufficient capacity assignment" and returns 0.
# If the pony limit is exceeded, it prints "Exceeding pony limit" and returns 0.
# If the path is valid and all checks pass, it prints "None" and returns 0.

# The code also defines a main() function which calls the check_path() function with different inputs
# and prints the results.
