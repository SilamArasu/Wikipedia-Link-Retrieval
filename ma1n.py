import requests,re
import sys,pickle
import time,os
from syn import related_terms,comp

# Constructing a valid Wikipedia URL
terms=sys.argv[1:]
terms[0]=terms[0].capitalize()
term='_'.join(terms)
url="https://en.wikipedia.org/wiki/"+term

# Fetching the webpage by URL
print("Fetching %s"%(url))
req=requests.get(url)
req.raise_for_status()  # Raises error if webpage cannot be fetched
print("Done")
time.sleep(1)

# Filtering the wiki links
text=req.text
result=set()        # No duplicates
link=re.findall(r'''(["][^"]+["]+)''',text)     # Filters strings between qoutes("")
print("Filtering the URLs")
time.sleep(1)
wiki=re.compile(r'''(/wiki/[^%][a-zA-Z_%0-9]+(\((.*?)\))?[a-zA-Z_%0-9]*)''',re.VERBOSE|re.IGNORECASE)   # Words that starts with wiki (only wiki articles)
for x in link:
    y= wiki.search(x)
    if y !=None :
        result.add(y.group(0))      #matched term
result={ "https://en.wikipedia.org"+x for x in result }
print("Total : "+str(len(result))+" results")
time.sleep(1)
for x in result:
    print(x)
    time.sleep(0.02)
time.sleep(1)

# Finding the terms related to user given words
print("Finding related terms...")
synonyms = related_terms(term)
print("Done")
time.sleep(1)
for x in synonyms:
    print("https://en.wikipedia.org/wiki/"+x)
    time.sleep(0.01)

# Retrieve words from user's search history and prints the words which have similarity to the user given word
try:
    file = open("dat", 'rb')
    b = pickle.load(file)
    pos = []
    for x in b:
        if(comp(term,x)):
            pos.append(x)

    if(len(pos)>0):
        print("Based on your search terms")
        for x in pos:
            print("https://en.wikipedia.org/wiki/"+x)
    file.close()
except IOError:
    os.system('touch dat')  # Creates empty file 'dat'
    file = open("dat", 'rb')
except EOFError:
    pass

# Saves the current term into the user's history
file = open("dat", 'wb')
term = [term,]
pickle.dump(term,file)
file.close()
