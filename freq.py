import sys
f=open(sys.argv[1])
dic={}
for line in f:
     for word in line.split():
          if word not in dic:
               dic[word] = 0
          if word in dic:
               dic[word] += 1
for res in dic:
     print("     ",dic[res],res)

