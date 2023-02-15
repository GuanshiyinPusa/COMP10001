def middle_words(word_list):
    n = len(word_list)
    ind = n // 2
    return [word_list[ind - 1], word_list[ind]] if n % 2 == 0 else [word_list[ind]]
