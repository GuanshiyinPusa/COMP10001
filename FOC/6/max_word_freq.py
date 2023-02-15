freq = {"hello": 3, "world": 5, "day":2,"a":10}

def max_word_freq(freq):
    most_common_word, max_freq = '',0
    for word, freq in freq.items():
        if freq > max_freq:
            max_freq = freq
            most_common_word = word
    return most_common_word

print(max_word_freq(freq))
