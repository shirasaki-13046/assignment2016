import sys
import shelve
from nltk.tokenize import sent_tokenize,word_tokenize

file=open(sys.argv[1]).read()
lines=sent_tokenize(file)
dic1=shelve.open("shelve_file2")
dic2={}

for line in lines:
    words=word_tokenize(line)
    for word in words:
        if word not in dic1:
            dic1[word]=len(dic1)+1

for line in lines:
    words=word_tokenize(line)
    for word in words:
        if dic1[word] in dic2:
            dic2[dic1[word]]+=1
        else:
            dic2[dic1[word]]=1

for res in dic2:
    print(res,":",dic2[res]," ",end="")
 
#dic1={}
#dic2={}
#i=0
#for line in lines:
#    words=word_tokenize(line)
#    for word in words:
#        if word in dic1:
#            dic1[word]+=1
#            dic2[dic[word]]=dic1[word]
#        else:
#            dic1[word]=1
#            dic2[dic[word]]=dic1[word]
#print(dic2)


