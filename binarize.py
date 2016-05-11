import sys

file=open(sys.argv[1]).read().split()
for num in file:
    if int(num) >= 4:
        print("1")
    else:
        print("-1")
