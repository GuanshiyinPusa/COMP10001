from collections import defaultdict as dd

def count_trigrams(document):
    """ count_trigrams takes a string and returns a dictionary of the
    counts of trigrams within the document. """

    tri_dict = dd(float)
    for i in range(len(document) - 2):
        trigram = document[i:i + 3]
        tri_dict[trigram] += 1
    return tri_dict