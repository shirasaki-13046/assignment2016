import sys
file=open(sys.argv[1]).readlines()
test_file=open(sys.argv[2]).readlines()

#i番目のレビューのタプルを作る
def read_instance(i):
    vector_list=[]
    review=file[i]
    label_sp=review.split("  ")
    label=label_sp[0]
    vectors=label_sp[1].rstrip().split(" ")
    for vector in vectors:
        youso=vector.split(":")
        vector_tup=(youso[0],youso[1])
        vector_list.append(vector_tup)
    res=(label,vector_list)
    vector_list=[]
    return res

#i番目のレビューをリストに入れ、最大インデックスを抽出
def read_data():
    max_index=1
    train_data=[]
    for i in range(len(file)):
        review=read_instance(i)
        sosei=review[1]
        sosei_max=max(sosei,key=(lambda x: int(x[0])))
        review_max = int(sosei_max[0])
        if int(review_max) > int(max_index):
            max_index=review_max
        train_data.append(review)
        i=i+1


    test_list=[]
    test_data=[]
    for j in range(len(test_file)):
        review=test_file[j]
        label_sp=review.split("  ")
        label=label_sp[0]
        vectors=label_sp[1].rstrip().split(" ")
        for vector in vectors:
            youso=vector.split(":")
            vector_tup=(youso[0],youso[1])
            test_list.append(vector_tup)
        res=(label,test_list)        
        test_data.append(res)
        test_list=[]
    return (train_data,max_index,test_data)


#素性ベクトルを足す
def add_fv(i):
    for k in range(len(train_data[i][1])):
        sosei=train_data[i][1][k]
        index=int(sosei[0])
        hindo=int(sosei[1])
        weight_vector[index]=weight_vector[index]+hindo

#素性ベクトルを引く
def sub_fv(i):
    for k in range(len(train_data[i][1])):
        sosei=train_data[i][1][k]
        index=int(sosei[0])
        hindo=int(sosei[1])
        weight_vector[index]=weight_vector[index]-hindo

#内積の計算
def mult_fv(i):
    naiseki=0
    for j in range(len(train_data[i][1])):
        sosei=train_data[i][1][j]
        index=int(sosei[0])
        hindo=int(sosei[1])
        if index <= max_index:
            naiseki_1=weight_vector[index]*hindo
            naiseki+=naiseki_1
    return naiseki

#ベクトルの更新
def update_weight():
    for i in range(len(train_data)):
        naiseki_2=int(mult_fv(i))
        label=int(train_data[i][0])
        if naiseki_2 * label <= 0:
            if label > 0:
                add_fv(i)
            else:
                sub_fv(i)

#結果の計算
def evaluate():
    naiseki=0
    seikai=0
    instance=0
    for i in range(len(test_data)):
        label=int(test_data[i][0])
        for j in range(len(test_data[i][1])):
            sosei=test_data[i][1][j]
            index=int(sosei[0])
            hindo=int(sosei[1])
            if index <= max_index:
                naiseki_single=weight_vector[index]*hindo
                naiseki+=naiseki_single
        if (naiseki * label) > 0:
            seikai+=1
        instance+=1
        naiseki=0
    seikairitsu=(seikai/instance)*100
    return (seikai,instance,seikairitsu)

weight=[]
read_data=read_data()
max_index=read_data[1]
for dim in range(int(max_index)+1):
    weight.append(0)

weight_vector=weight
train_data=read_data[0]
test_data=read_data[2]

for r in range(5000):
    update_weight()
print(evaluate())



#for r in range(1000):
#    vector_result=update_weight()
#    if r == 0:
#        result=evaluate(vector_result)
#        print("正解数 : ",result[0],"\n","インスタンス数 : ",result[1],"\n","正解率 : ",result[2],"%")
#    if r == 50:
#        result=evaluate(vector_result)
#        print("正解数 : ",result[0],"\n","インスタンス数 : ",result[1],"\n","正解率 : ",result[2],"%")
#    if r == 200:
#        result=evaluate(vector_result)
#        print("正解数 : ",result[0],"\n","インスタンス数 : ",result[1],"\n","正解率 : ",result[2],"%")
#    if r == 400:
#        result=evaluate(vector_result)
#        print("正解数 : ",result[0],"\n","インスタンス数 : ",result[1],"\n","正解率 : ",result[2],"%")
#    if r == 800:
#        result=evaluate(vector_result)
#        print("正解数 : ",result[0],"\n","インスタンス数 : ",result[1],"\n","正解率 : ",result[2],"%")
#   if r == 1000:
#        result=evaluate(vector_result)
#        print("正解数 : ",result[0],"\n","インスタンス数 : ",result[1],"\n","正解率 : ",result[2],"%")
