from hidden_lib import count_trigrams
from hidden_lib import train_classifier

default_lang_counts = train_classifier('train.csv')

def score_document(document, lang_counts=default_lang_counts):
    """ score_document takes a string document and a dictionary of language 
    counts per language stored in lang_counts. It returns a dictionary of 
    scores for the document for each language.
    """
    doc_text = open(document, 'r').read()
    doc_counts = count_trigrams(doc_text)
    languages = lang_counts.keys()
    score_dict = {}
    for lang in languages:
        
        # calculate the score for this language by performing a dot product
        score = 0.0
        for trigram in doc_counts.keys():
            score += doc_counts[trigram] * lang_counts[lang][trigram]
            
        score_dict[lang] = score
    return score_dict