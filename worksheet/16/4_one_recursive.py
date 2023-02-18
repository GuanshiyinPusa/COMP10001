def longest_word(my_list):
    if not my_list:
        return None
    if len(my_list) == 1:
        return my_list[0]
    first_word = my_list[0]
    rest_words = my_list[1:]
    longest_rest = longest_word(rest_words)
    if len(first_word) > len(longest_rest):
        return first_word
    else:
        return longest_rest
