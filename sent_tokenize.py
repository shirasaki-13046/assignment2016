import sys
from nltk.tokenize import sent_tokenize
f=open(sys.argv[1])
print(sent_tokenize(f.read()))
