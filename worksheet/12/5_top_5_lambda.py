def top5_words(text):
    tally = {}
    MOBY = text.split()
    for char in MOBY:
        tally[char] = tally.get(char, 0) + 1
    if len(tally) < 5:
        return sorted(tally, key=lambda x: (-tally[x], x))
    else:
        return sorted(tally, key=lambda x: (-tally[x], x))[:5]