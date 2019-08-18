import requests,re
import sys,pickle
import time,os
from syn import related_terms,comp
terms=sys.argv[1:]
terms[0]=terms[0].capitalize()
term='_'.join(terms)


url="https://en.wikipedia.org/wiki/"+term
print("Fetching %s"%(url))
req=requests.get(url)
req.raise_for_status()
print("Done")
time.sleep(1)
text=req.text
result=set()        #no duplicates
link=re.findall(r'''(["][^"]+["]+)''',text)     #strings between qoutes
print("Filtering the URLs")
time.sleep(1)
wiki=re.compile(r'''(/wiki/[^%][a-zA-Z_%0-9]+(\((.*?)\))?[a-zA-Z_%0-9]*)''',re.VERBOSE|re.IGNORECASE)   #starts with wiki (only wiki articles)
for x in link:
    y= wiki.search(x)
    if y !=None :
        result.add(y.group(0))      #matched term
print("Filtering Wiki articles")
result={ "https://en.wikipedia.org"+x for x in result }
print("Total : "+str(len(result))+" results")
time.sleep(1)
for x in result:
    print(x)
    time.sleep(0.02)
time.sleep(1)
print("Finding related terms...")
synonyms = related_terms(term)
print("Done")
time.sleep(1)
for x in synonyms:
    print("https://en.wikipedia.org/wiki/"+x)
    time.sleep(0.01)


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
    os.system('touch dat')
    file = open("dat", 'rb')
except EOFError:
    pass

file = open("dat", 'wb')
term = [term,]
pickle.dump(term,file)
file.close()
