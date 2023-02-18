import csv

from collections import defaultdict as dd
from math import sqrt

from hidden_lib import count_trigrams

def normalise(counts_dict):
    """ normalise takes a dictionary of trigram counts counts_dict and
    normalises it by it's length."""
    mag = sqrt(sum([x**2 for x in counts_dict.values()]))
    return dd(int, {key: value / mag for (key, value) in counts_dict.items()})

def train_classifier(training_set):
    """ train_classifier takes a csv file training_set and returns a dictionary 
    containing dictionaries for each language label with the average frequency 
    of occurrence of trigrams per language. 
    """
    tset_reader = csv.reader(open(training_set, 'r'))
    # find the counts for each language 
    lang_dict = {}
    for row in tset_reader:
        (lang, text) = row
        if lang not in lang_dict:
            lang_dict[lang] = dd(float)
        trigram_dict = count_trigrams(text)
        for trigram in trigram_dict:
            lang_dict[lang][trigram] += trigram_dict[trigram]
    # normalise over the number of trigrams per language
    for lang, count_dict in lang_dict.items():
        lang_dict[lang] = normalise(count_dict)
    return lang_dict