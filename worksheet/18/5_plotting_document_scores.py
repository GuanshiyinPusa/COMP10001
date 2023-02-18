# from plotter import plot_scores
from hidden_lib import train_classifier
from hidden_lib import count_trigrams

default_lang_counts = train_classifier('train.csv')

def score_document(document, lang_counts=default_lang_counts):
    """ score_document takes a string document and a dictionary of language 
    counts per language stored in lang_counts. It returns a dictionary of 
    scores for the document for each language.
    """
    doc_counts = count_trigrams(document)
    languages = lang_counts.keys()
    score_dict = {}
    for lang in languages:
        
        # calculate the score for this language by performing a dot product
        score = 0.0
        for trigram in doc_counts.keys():
            score += doc_counts[trigram] * lang_counts[lang][trigram]
            
        score_dict[lang] = score
    return score_dict

def select_scores(langs, document, lang_counts=default_lang_counts):
    '''select_scores selects the scores for the string document and languages
    langs and returns them in a list with the list langs.'''
    scores = score_document(document, lang_counts)
    select_scores = [scores[lang] for lang in langs]
    return (langs, select_scores)