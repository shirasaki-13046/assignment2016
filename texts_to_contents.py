import sys
import gzip
import nltk
from nltk.tokenize import RegexpTokenizer
import shelve
import MeCab

dic_junban=shelve.open("naiyougo_shelve")
dic_hindo={}
mec=MeCab.Tagger()
jp_sent_tokenizer=nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')
file=gzip.open(sys.argv[1]).read().decode("utf-8").split("\n")
i=0

for txt in range(len(file)):
    sent=jp_sent_tokenizer.tokenize(file[i])
    i=i+1
    j=0
    for line in range(len(sent)):
        words=mec.parse('')
        node=mec.parseToNode(sent[j])
        j=j+1
        while node:
            hinshi=node.feature.split(",")
            hyousou=node.surface
            if hinshi[0]=="名詞" or hinshi[0]=="動詞" or hinshi[0]=="形容詞" or hinshi[0]=="形容動詞" or hinshi[0]=="副詞":
                if hyousou not in dic_junban:
                    dic_junban[hyousou]=len(dic_junban)+1
            node=node.next

i=0
for txt in range(len(file)):
    sent=jp_sent_tokenizer.tokenize(file[i])
    i=i+1
    j=0
    for line in range(len(sent)):
        words=mec.parse('')
        node=mec.parseToNode(sent[j])
        j=j+1
        while node:
            hyousou=node.surface
            hinshi=node.feature.split(",")
            if hinshi[0]=="名詞" or hinshi[0]=="動詞" or hinshi[0]=="形容詞" or hinshi[0]=="形容動詞" or hinshi[0]=="副詞":
                if dic_junban[hyousou] not in dic_hindo:
                    dic_hindo[dic_junban[hyousou]]=1
                else:
                    dic_hindo[dic_junban[hyousou]]+=1
            node=node.next
    for item in dic_hindo:
        print(str(item)+":"+str(dic_hindo[item]),end=" ")
    print("")
    dic_hindo={}
