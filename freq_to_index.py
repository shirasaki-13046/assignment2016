import sys
from nltk.tokenize import sent_tokenize,word_tokenize
file=open(sys.argv[1]).read()
lines=sent_tokenize(file)
dic1={}
dic2={}
i=0
for line in lines:
    words=word_tokenize(line)
    for word in words:
        if word in dic1:
            dic1[word]+=1
            dic2[word]+=0
        else:
            dic1[word]=1
            dic2[word]=1+i
            i=i+1

res=sorted(dic2.items(),key=lambda x: x[1])

for fin in res:
    print(fin[0],fin[1])

#print(dic1)
#print(dic2)


#for res in dic1:
#    A=(res,dic1[res])
#for num in dic2:
#    B=(num,dic2[num])    
#print(B)

