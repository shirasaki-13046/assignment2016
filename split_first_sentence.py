import sys
import gzip
import nltk
from nltk.tokenize import RegexpTokenizer
i=0
jp_sent_tokenizer=nltk.RegexpTokenizer(u'[^！？。]*[！？。]')
file=gzip.open(sys.argv[1]).read()
txts=file.decode("utf-8").split()
txt=jp_sent_tokenizer.tokenize(txts[0])
for sent in range(len(txt)):
    print(txt[i])
    i=i+1
