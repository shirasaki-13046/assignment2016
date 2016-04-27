import CaboCha
c=CaboCha.Parser()
txt="豊工に行っています。"
tree=c.parse(txt)
branch=(tree.toString(CaboCha.FORMAT_TREE)).split()
for bunsetsu in branch:
    if "EOS" not in bunsetsu:
        print(bunsetsu)
