import CaboCha
import sys
c = CaboCha.Parser()
txt="豊工に行っています。"
tree=c.parse(txt)

for i in range(tree.chunk_size()):
    cnk=tree.chunk(i)
    for j in range(cnk.token_pos,cnk.token_pos+cnk.token_size):
        tkn=tree.token(j)
        print(tkn.surface,"\t",tkn.ne)
    print("\n",end="")

#print(tree.toString(CaboCha.FORMAT_LATTICE).split())

#for i in range(tree.token_size()):
#    tkn=tree.token(i)
#        print(tkn.surface,"\t",tkn.ne)
