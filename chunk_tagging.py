import sys
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tag import SennaTagger,SennaChunkTagger

f=open(sys.argv[1])
lines=sent_tokenize(f.read())
words=word_tokenize(lines[0])
chunk_tagger=SennaChunkTagger('/usr/share/senna-v2.0')
ch=chunk_tagger.tag(words)

for words in ch:    
    if "B-" in words[1]:
        B=("\n"+words[1].strip("B-")+" "+words[0])
        print(B,end="")
    else:
        print(" "+words[0],end="")
 
