import copy

# check
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


# def do_a(pony, next_energy, log_value):
#     for before in range(pony[0]):
#         before_pony = log_value[before]
#         if before_pony[-1][-1] == pony[-1][-1]:
#             if pony[-1][0] >= next_energy:
#                 before_pony[-1][0] = next_energy
#                 pony[-1][0] = pony[-1][0] - next_energy

# havent check
# def do_a(pony, next_energy, log_value):
#     last_p, last_e = pony[-1]
#     for i, before_pony in enumerate(log_value):
#         if before_pony[-1][-1] == last_e:
#             for before_p in before_pony:
#                 if before_p[-1] == last_e and before_p[0] >= next_energy:
#                     before_p[0] -= next_energy
#                     last_p -= next_energy
#                     break
#             else:
#                 continue
#             break


# check
def do_pony(timestep, path, distance_list, log):
    log_value = []
    ponies = copy.deepcopy(log[timestep - 1])
    for pony in ponies:
        location = pony[-1][-1]
        if pony[0] < timestep and location != path[-1]:
            path_index = path.index(location)
            next_energy = distance_list[path_index]
            # if pony[1] == "a":
            #     do_a(pony, next_energy, log_value)
            if pony[-1][0] >= next_energy:
                next_step = path_index + 1
                pony[-1][0] = pony[-1][0] - next_energy
                pony[-1][-1] = path[next_step]
        log_value.append(pony)
    log[timestep] = log_value


# check
def done(log, timestep, ponies):
    if log[timestep] == log[timestep - 1] and timestep - 1 > max(pony[0] for pony in ponies):
        del log[timestep]
        return False
    return True

# check    
def climb(path, elevations, ponies):
    timestep = 0
    log = {timestep : ponies}
    distance_list = find_distance(elevations, path)
    check_done = True
    max_timesteps = len(path) * len(ponies) # Set a maximum number of timesteps based on the number of ponies and the length of the path
    while check_done and timestep < max_timesteps: # Add a check to ensure the loop does not run indefinitely
        timestep += 1
        do_pony(timestep, path, distance_list, log)
        check_done = done(log, timestep, ponies)
    return log
