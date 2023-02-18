def mutual_friends(list1, list2):
    st1 = set(list1)
    st2 = set(list2)
    return len(st1.intersection(st2))
