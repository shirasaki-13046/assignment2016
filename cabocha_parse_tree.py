import CaboCha
c=CaboCha.Parser()
txt="豊工に行っています。"
tree=c.parse(txt)
print(tree.toString(CaboCha.FORMAT_TREE))
