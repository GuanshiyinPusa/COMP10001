def longest_word(my_list):
    if not my_list:
        return None
    if len(my_list) == 1:
        return my_list[0]
    else:
        midpoint = len(my_list)//2
        a = longest_word(my_list[midpoint:])
        b = longest_word(my_list[:midpoint])
        if len(a) > len(b):
            return a
        else:
            return b
