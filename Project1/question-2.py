# 1. Assignment is Superior if it has lower total unused pony capacity
# 2. Smaller differences between the capacity of two assigned ponies are preferred
# 3. If moves are different, prefer the one with greater elevation raise
# (Reason: the greater part of a job is nicely equipped, the better)
# Prefer moves into lower* value (x,y) coordinates (This is just to make the result deterministic)

# pony_capacities = [17, 37, 73]
# journey_path = [(0,0), (0,1), (0,2), (0,3), (1,3), (1,4), (1,5)]
# village_elevations = [[ 100, 200, 300, 400, 100, 600], [0, 100, 200, 300, 400, 500 ]]

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


def assign_pony_to_path(elevations, path, capacities):
    final_elevation = [elevations[x][y] for x, y in path]
    distance = [(final_elevation[i + 1] - final_elevation[i])
                for i in range(len(final_elevation) - 1)]
    ans_capacity = []
    for m in distance:
        possible_capacities = [(capacities[i], capacities[j]) for i in range(len(capacities)) for j in
                               range(i, len(capacities))]
        ans_capacity.append(closest_greater_or_equal_number(possible_capacities, m))
    return ans_capacity


pony_capacities = [17, 37, 73]
journey_path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)]
pony_assignments = [(73, 73)] * 6
village_elevations = [[100, 200, 300, 400, 100, 600],
                      [0, 100, 200, 300, 400, 500]]
lower_village_elevations = [[10, 20, 30, 40, 10, 60], [0, 10, 20, 30, 40, 50]]
another_journey_path = [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]
impossible_journey_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5)]


def main():
    print(assign_pony_to_path(village_elevations, journey_path, pony_capacities))
    print("\n")
    print(assign_pony_to_path(lower_village_elevations, journey_path, pony_capacities))
    print("\n")
    print(assign_pony_to_path(village_elevations, another_journey_path, pony_capacities))
    print("\n")
    print(assign_pony_to_path(village_elevations, impossible_journey_path, pony_capacities))


if __name__ == "__main__":
    main()

# This code defines a function "assign_pony_to_path" which takes in three arguments: elevations, path, and capacities.

# It first calculates the distance between villages by finding the final elevations for each point in the journey path,
# and then calculating the difference between each consecutive point.

# It then iterates through the distance array, and for each element, it creates a list of possible capacities by taking
# the combinations of two elements in the capacities list.

# It then finds the closest greater or equal number to the current distance element by calling the function
# "closest_greater_or_equal_number", and appends it to the ans_capacity list.

# Finally, it returns the ans_capacity list.

# The function "closest_greater_or_equal_number" takes two arguments: an array of tuples and a target number.

# It iterates through the array and finds the tuple whose sum of elements is greater than or equal to the target number
# and has the minimum difference from the target number.

# The main function calls assign_pony_to_path with different arguments for elevations, path, and capacities and print
# the result.
