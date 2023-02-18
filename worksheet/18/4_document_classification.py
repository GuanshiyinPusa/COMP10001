from hidden_lib import train_classifier
from hidden_lib import score_document

# Tolerance for detecting null predictions
TOL = 1e-10

# We train the classifier here
default_lang_counts = train_classifier('train.csv')

def classify_doc(document, lang_counts=default_lang_counts):
    """ classify_document returns the language of the document according to the 
    dictionary of language counts lang_counts.
    """
    scores = score_document(document, lang_counts)
    
    vals = sorted(scores.values(), reverse=True)
    if abs(vals[1] - vals[0]) <= TOL:
        return "English"
    else:
        return max([(score, lang) for (lang, score) in scores.items()])[1]