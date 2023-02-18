from plotter import plot_pnr
from hidden_lib import classify_doc
from hidden_lib import train_classifier
from collections import defaultdict as dd
import csv
# Increase the field size limit (we have big files)
csv.field_size_limit(int(1e7))

# We train the classifier here
default_lang_counts = train_classifier('small_train.csv')

def calc_precision(test_set):
    """calc_precision takes the filename of a csv file test_set and returns 
    a dictionary of the precision of the classifier per language."""
    
    # iterate through the test set, tallying the number of predictions for each 
    # language and the number of those which were correct
    t_reader = csv.reader(open(test_set, 'r'))
    pred_counts = dd(int)
    correct_counts = dd(int)
    for row in t_reader:
        (lang, doc) = row
        pred = classify_doc(doc, default_lang_counts)
        pred_counts[pred] += 1
        correct_counts[lang] += (lang == pred)
    
    # Use the tallies to find the precision for each language.
    precision_dict = dd(float)
    for (lang, pcount) in pred_counts.items():
        precision_dict[lang] = float(correct_counts[lang]) / pcount
    
    return precision_dict

def calc_recall(test_set):
    """calc_recall takes the filename of a csv file test_set and returns a
    dictionary of the recall of the classifier per language."""
    
    # iterate through the test set, recording the number of documents in each 
    # language as well as the number correctly classified.
    t_reader = csv.reader(open(test_set, 'r'))
    lang_counts = dd(int)
    correct_counts = dd(int)
    for row in t_reader:
        (lang, doc) = row
        lang_counts[lang] += 1
        pred = classify_doc(doc, default_lang_counts)
        correct_counts[lang] += (pred == lang)
    # find the recall per language
    recall_dict = dd(float)
    for (lang, count) in lang_counts.items():
        recall_dict[lang] = float(correct_counts[lang]) / count
    
    return recall_dict