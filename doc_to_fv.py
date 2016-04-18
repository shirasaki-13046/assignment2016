import sys
import shelve
from nltk.tokenize import sent_tokenize,word_tokenize

file=open(sys.argv[1]).read()
lines=sent_tokenize(file)
dic=shelve.open("shelve_file")
dic1={}
dic2={}
i=0
for line in lines:
    words=word_tokenize(line)
    for word in words:
        if word in dic1:
            dic1[word]+=1
            dic2[dic[word]]=dic1[word]
        else:
            dic1[word]=1
            dic2[dic[word]]=dic1[word]
print(dic2)


