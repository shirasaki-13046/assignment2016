import sys
import shelve
from nltk.tokenize import sent_tokenize,word_tokenize
#保存ファイルの指定
dic=shelve.open("shelve_file")

lines=sent_tokenize(open(sys.argv[1],'r').read())
i=len(dic)
for line in lines:
    words=word_tokenize(line)
    for word in words:
        if word in dic:
            dic[word]+=0
        else:
            dic[word]=1+i
            i=i+1

dic.close
#実行結果を指定したファイルへ保存
#newfile=file.update()

#res=sorted(dic.items(),key=lambda x: x[1])
#print(res[1],res[0])
