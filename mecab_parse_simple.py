import sys
import MeCab
from nltk.tokenize import word_tokenize

m=MeCab.Tagger()
k=m.parse("豊工に行っています。").split("\n")
for words in k:
    wordtab=words.split("\t")
    if len(wordtab)>1:
        word=wordtab[1].split(",")
        if len(word)>1:
            print(wordtab[0]+"\t"+word[0]+"\t"+word[6])

