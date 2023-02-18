def approximate_song(filename):
    with open(filename) as fp:
        long = []
        huge = set()
        for line in fp:
            words = line.split()
            long.extend(words)
            huge.update(words)
    
    dic = {word: long.count(word) for word in huge}
    sorted_words = sorted(dic, key=dic.get)
    return sorted_words[-1]