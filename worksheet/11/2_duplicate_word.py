from collections import Counter

def repeat_word_count(text, n):
    word_counts = Counter(text.split())
    repeated_words = sorted([word for word, count in word_counts.items() if count >= n])
    return repeated_words
