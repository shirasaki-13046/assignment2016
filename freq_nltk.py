import sys
from nltk.tokenize import sent_tokenize,word_tokenize

f=open(sys.argv[1])
lines=sent_tokenize(f.read())
dic={}
for words in lines:
    word=word_tokenize(words)
    for freq in word:
        if freq in dic:
            dic[freq]+=1
        else:
            dic[freq]=1
for res in dic:
    print("     ",dic[res],res)
