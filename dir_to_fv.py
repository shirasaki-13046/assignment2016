import os
import sys
from nltk import sent_tokenize,word_tokenize
import shelve

dic=shelve.open("shelve_dir")
filenames=os.listdir(sys.argv[1])
for files in filenames:
    file=open(sys.argv[1]+'/'+files).read()
    lines=sent_tokenize(file)
    for line in lines:
        words=word_tokenize(line)
        for word in words:
            if word not in dic:
                dic[word]=len(dic)+1

for files in filenames:
    dic1={}
    file=open(sys.argv[1]+'/'+files).read()
    lines=sent_tokenize(file)
    for line in lines:
       words=word_tokenize(line)
       for word in words:
           if dic[word] in dic1:
               dic1[dic[word]]+=1
           else:
               dic1[dic[word]]=1
    for item in dic1:
        print(str(item)+":"+str(dic1[item]),end=" ")
    print("")
dic.close
