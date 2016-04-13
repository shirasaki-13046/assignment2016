import sys
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tag import SennaTagger
f=open(sys.argv[1],'r')
lines=sent_tokenize(f.read())
tagger=SennaTagger('/usr/share/senna-v2.0')
words=word_tokenize(lines[1])    
print(tagger.tag(words))
