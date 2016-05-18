import sys
file=open(sys.argv[1]).readlines()
def read_instance(i):
    vector_list=[]
    for review_count in range(len(file)):
        review=file[i]
        label_sp=review.split("  ")
        label=label_sp[0]
        vectors=label_sp[1].rstrip().split(" ")
        for vector in vectors:
            youso=vector.split(":")
            index=youso[0]
            hindo=youso[1]
            vector_tup=(index,hindo)
            vector_list.append(vector_tup)
        res=(label,vector_list)
        vector_list=[]
        return(res)

def read_data():
    vector_list=[]
    i=0
    index_max=1
    for review_cont in range(len(file)):
        review=read_instance(i)
        sosei=review[1]
        sosei_max=max(sosei,key=(lambda x: int(x[0])))
        review_max = int(sosei_max[0])
        if int(review_max) > int(index_max):
            index_max=review_max
        vector_list.append(review)
        i=i+1
    return(index_max)

train_data=read_data()
max_index=read_data()

weight=[]
for dim in range(max_index+1):
    weight.append(0)
print(weight)
