import sys
import gzip
import nltk
from nltk.tokenize import RegexpTokenizer
import shelve
import MeCab
dic_junban={}
dic_hindo={}
dic_sort={}
sentence=[]
mec=MeCab.Tagger()
jp_sent_tokenizer=nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')
file=gzip.open(sys.argv[1]).read().decode("utf-8").split("\n")
i=0
h=0

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
            sentence.append(hyousou)
            node=node.next
        for ngram in range(len(sentence)):
            unigram=sentence[h]
            if h <= len(sentence)-2:
                bigram=sentence[h]+sentence[h+1]
            if h <= len(sentence)-3:
                trigram=sentence[h]+sentence[h+1]+sentence[h+2]
            if unigram not in dic_junban:
                dic_junban[unigram]=len(dic_junban)+1
            if bigram not in dic_junban:
                dic_junban[bigram]=len(dic_junban)+1
            if trigram not in dic_junban:
                dic_junban[trigram]=len(dic_junban)+1
            
            if dic_junban[unigram] not in dic_hindo:
                dic_hindo[dic_junban[unigram]]=1
            else:
                dic_hindo[dic_junban[unigram]]+=1

            if dic_junban[bigram] not in dic_hindo:
                dic_hindo[dic_junban[bigram]]=1
            else:
                dic_hindo[dic_junban[bigram]]+=1

            if dic_junban[trigram] not in dic_hindo:
                dic_hindo[dic_junban[trigram]]=1
            else:
                dic_hindo[dic_junban[trigram]]+=1
                
            h=h+1
        sentence=[]
        h=0
    for items in sorted(dic_hindo.items(),key=lambda x: x[0]):
        print(str(items[0])+":"+str(items[1]),end=" ")
    print("")
    dic_hindo={}
#    print(sorted(dic_junban.items(),key=lambda x:(x[1])))
#    break


#i=0
#h=0
#for txt in range(len(file)):
#    sent=jp_sent_tokenizer.tokenize(file[i])
#    i=i+1
#    j=0
#    for line in range(len(sent)):
#        words=mec.parse('')
#        node=mec.parseToNode(sent[j])
#        j=j+1
#        while node:
#            hyousou=node.surface
#            sentence.append(hyousou)
#            node=node.next
#        for ngram in range(len(sentence)):
#            unigram=(sentence[h])
#            if h <= len(sentence)-2:
#                bigram=sentence[h]+sentence[h+1]
#            if h <= len(sentence)-3:
#                trigram=sentence[h]+sentence[h+1]+sentence[h+2]
#            
#            if dic_junban[unigram] not in dic_hindo:
#                dic_hindo[dic_junban[unigram]]=1
#            else:
#                dic_hindo[dic_junban[unigram]]+=1
#
#            if dic_junban[bigram] not in dic_hindo:
#                dic_hindo[dic_junban[bigram]]=1
#            else:
#                dic_hindo[dic_junban[bigram]]+=1
#
#            if dic_junban[trigram] not in dic_hindo:
#                dic_hindo[dic_junban[trigram]]=1
#            else:
#                dic_hindo[dic_junban[trigram]]+=1
#
#            h=h+1
#        sentence=[]
#        h=0
#
#    for item in dic_hindo:
#        print(str(item)+":"+str(dic_hindo[item]),end=" ")
#    print("")
#    dic_hindo={}
