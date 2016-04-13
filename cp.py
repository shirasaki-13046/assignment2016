import sys

source=open(sys.argv[1])
dest=open(sys.argv[2],"w")

for l in source:
    dest.write(l)
source.close
dest.close
