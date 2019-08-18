import nltk
from nltk.corpus import wordnet

synonyms = []
antonyms = []
def related_terms(word):
 for syn in wordnet.synsets(word):
    for l in syn.lemmas():
        synonyms.append(l.name())
 //print(set(synonyms))
 return set(synonyms)


# Let's compare the noun of "ship" and "boat:"
def comp(a,b):
    w1 = wordnet.synset(a+'.n.01')  # v here denotes the tag verb
    w2 = wordnet.synset(b+'.n.01')
    a = w1.wup_similarity(w2)
    if(a>0.5):
        return True
    else:
        False
