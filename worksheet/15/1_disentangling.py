def aha(minval, maxval):
    l = []
    for i in range(minval, maxval + 1):
        l.append(i**2 % 10)
    return l
