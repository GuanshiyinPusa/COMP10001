def sorted_words(wordlist):
    emp = [i for i in wordlist if list(i) == sorted(i)]
    emp.sort()
    return emp

