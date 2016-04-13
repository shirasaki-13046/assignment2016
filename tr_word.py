import sys
f=open(sys.argv[1])
for line in f:
    newline=line.strip()
    for word in newline.split(" "):
        print (word)
