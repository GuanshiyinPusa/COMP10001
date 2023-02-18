def maxby(intlist):
    if not intlist:
        return None, None
    elif len(intlist) == 1:
        return intlist[0], None
    else:
        sorted_intlist = sorted(intlist, reverse=True)
        maxnum = sorted_intlist[0]
        bymargin = maxnum - sorted_intlist[1] if sorted_intlist[0] != sorted_intlist[1] else 0
        return maxnum, bymargin
