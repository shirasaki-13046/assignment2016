import sys
f=open(sys.argv[1])
for l in f:
    if sys.argv[2] in l:
        print(l,end="")
f.close
