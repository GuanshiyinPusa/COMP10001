# # data samples: 1
#
# pony_capacities = [17, 37, 73]
# journey_path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)]
# pony_assignments = [(73, 73)] * 6
# village_elevations = [[100, 200, 300, 400, 100, 600], [0, 100, 200, 300, 400, 500]]
# # None
#
# journey_path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 6)]
# # ((1, 6), 'Cell coordinate is out of bounds')
#
#
# journey_path = [(0, 1), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)]
# # ((0, 1), 'Path should start at (0,0) coordinate')
#
#
# pony_assignments = [(73, 17)] * 6
# journey_path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)]
# # ((0, 0), 'Insufficient capacity assignment')

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