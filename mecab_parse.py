import sys
import MeCab
m=MeCab.Tagger()
print(m.parse("豊工に行っています。"))

