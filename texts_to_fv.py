import sys
import gzip
import nltk
import MeCab
from nltk.tokenize import RegexpTokenizer

dic_junban={}
dic_hindo={}
i=0
mec=MeCab.Tagger()
jp_sent_tokenizer=nltk.RegexpTokenizer(u'[^！？。]*[！？。]')
file=gzip.open(sys.argv[1]).read()
texts=file.decode("utf-8").split()

for txt in range(len(texts)):
    sent=jp_sent_tokenizer.tokenize(texts[i])
    i=i+1
    j=0
    for line in range(len(sent)):
        words=mec.parse('')
        node=mec.parseToNode(sent[j])
        j=j+1
        while node:
            keitai=node.surface
            if keitai not in dic_junban:
                dic_junban[keitai]=len(dic_junban)+1
                dic_hindo[dic_junban[keitai]]=1
            else:
                dic_hindo[dic_junban[keitai]]+=1
            node=node.next
for item in dic_hindo:
    print(str(item)+":"+str(dic_hindo[item]),end=" ")
print("")
        



    
