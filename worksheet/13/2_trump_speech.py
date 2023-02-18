from collections import defaultdict

def count_lengths(text):
    word_lengths = defaultdict(int)
    words = text.split()
    for word in words:
        length = len(word)
        word_lengths[length] += 1
    return word_lengths

def top5_word_lengths(text):
    word_lengths = count_lengths(text)
    sorted_lengths = sorted(word_lengths.items(), key=lambda x: (-x[1], -x[0]))
    top5 = [length[0] for length in sorted_lengths[:5]]
    return top5