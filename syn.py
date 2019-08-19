import nltk
from nltk.corpus import wordnet

# Gets related terms from the nltk wordnet library
def related_terms(word):
 synonyms = set()
 for syn in wordnet.synsets(word):
    for l in syn.lemmas():
        synonyms.append(l.name())
 return set(synonyms)

# Computes the degree of similarity between two words
def comp(a,b):
    w1 = wordnet.synset(a+'.n.01')  # n here denotes the tag noun
    w2 = wordnet.synset(b+'.n.01')
    a = w1.wup_similarity(w2)
    if(a>0.5):
        return True
    else:
        False
