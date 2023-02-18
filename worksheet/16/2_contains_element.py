def contains_element(my_list, elem):
    if not my_list:
        return False
    elif my_list[0] == elem:
        return True
    else:
        return contains_element(my_list[1:], elem)