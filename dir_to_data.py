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
            if word in dic:
                dic[word]+=0
            else:
                dic[word]=len(dic)+1
label=-1
for files in filenames:
    dic1={}
    print(label," ",end="")
    file=open(sys.argv[1]+'/'+files).read()
    lines=sent_tokenize(file)
    for line in lines:
       words=word_tokenize(line)
       for word in words:
           if dic[word] in dic1:
               dic1[dic[word]]+=1
           else:
               dic1[dic[word]]=1
               
    for items in sorted(dic1.items(),key=lambda x: x[0]):
        print(str(items[0])+":"+str(items[1])+" ",end="")

#        print(str(item)+":"+str(dic1[item]),end=" ")

    print("")
dic.close
