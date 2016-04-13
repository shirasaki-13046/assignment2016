import sys
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

f=open(sys.argv[1],'r')

#sents=sent_tokenize(f.read())
#words=word_tokenize(sents)
#print(word_tokenize(sent_tokenize(f.read())))

lines=sent_tokenize(f.read())
for words in lines:
    print(word_tokenize(words))

#print(word_tokenize(sent_tokenize(f.read())))
