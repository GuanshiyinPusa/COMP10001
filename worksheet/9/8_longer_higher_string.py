def long_high_word(wordlist):
    return max(sorted(wordlist, key=len, reverse=True), key=lambda x: (len(x), x))
