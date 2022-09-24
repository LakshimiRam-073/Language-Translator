import nltk
from nltk.corpus import words
from nltk.metrics.distance import (
    edit_distance,
    jaccard_distance,
    )
from nltk.util import ngrams
import Levenshtein
#nltk.download('words')
import pandas



correct_spellings = words.words()
spellings_series = pandas.Series(correct_spellings)

def editreco(entries):

    outcomes = []
    for entry in entries:
        distances = ((Levenshtein.distance(entry,word), word)
                     for word in correct_spellings)
        closest = min(distances)
        outcomes.append(closest[1])

        '''for i in outcomes:
            if entry != outcomes:
                print("corrected words "+str(i))
            break'''
    return outcomes





