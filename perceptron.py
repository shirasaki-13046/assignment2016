import sys
import random
import math
from optparse import OptionParser
train_file=open(sys.argv[1]).readlines()
test_file=open(sys.argv[2]).readlines()

#i番目のレビューのタプルを作る
def read_instance(filename,i):
    vector_list=[]
    norm_bef=0
    review=filename[i]
    label_sp=review.split("  ")
    label=int(label_sp[0])
    vectors=label_sp[1].rstrip().split(" ")
    for vector in vectors:
        youso=vector.split(":")
        hindo=int(youso[1])
        norm_bef += hindo * hindo
    norm_bunbo=math.sqrt(norm_bef)
    for vector in vectors:
        youso=vector.split(":")
        index=int(youso[0])
        hindo=int(youso[1])
        if sys.argv[5] == str(1):
            norm_bunbo=1
        norm = hindo/norm_bunbo
        vector_tup=(index,norm)
        vector_list.append(vector_tup)
    bius=(int(0),int(sys.argv[4]))
    vector_list.append(bius)
    res=(label,vector_list)
    vector_list=[]
    return res

#i番目のレビューをリストに入れ、最大インデックスを抽出
def read_data(train_file,test_file):
    max_index=0
    train_data=[]
    for i in range(len(train_file)):
        review=read_instance(train_file,i)
        sosei=review[1]
        sosei_max=max(sosei,key=(lambda x: int(x[0])))
        review_max = int(sosei_max[0])
        if review_max > max_index:
            max_index=review_max
        train_data.append(review)
        i=i+1
    test_data=[]
    for i in range(len(test_file)):
        review=read_instance(test_file,i)
        sosei=review[1]
        test_data.append(review)
        i=i+1
    return (train_data,max_index,test_data)

#素性ベクトルを足す
def add_fv(i,train):
    for k in range(len(train)):
        index=train[k][0]
        hindo=train[k][1]
        weight[index]+=hindo
        upmath=hindo * nupdates[0]
        tmp_weight[index]+=upmath

#素性ベクトルを引く
def sub_fv(i,train):
    for k in range(len(train)):
        index=train[k][0]
        hindo=train[k][1]
        upmath=hindo * nupdates[0]
        tmp_weight[index]-=upmath
        weight[index]-=hindo

#内積の計算
def mult_fv(i,filename,weight_vector):
    naiseki=0
    for j in range(len(filename)):
        index=filename[j][0]
        hindo=filename[j][1]
        if index <= max_index:
            naiseki+=weight_vector[index] * hindo
    return naiseki

#ベクトルの更新
def update_weight():
    random.seed(0)
    random.shuffle(train_data)
    for i in range(len(train_data)):
        train=train_data[i][1]
        naiseki_2=mult_fv(i,train,weight)
        label=train_data[i][0]        
        if abs(naiseki_2) < float(sys.argv[6]) or naiseki_2*label<=0:
            nupdates[0]+=1
            if label > 0 :
                add_fv(i,train)
            else:
                sub_fv(i,train)
            for j in range(len(weight_vector_2)):
                weight_vector_2[j]+=weight[j]

#ベクトルの平均化
def averaged_weight():
    for i in range(len(weight)):
        ave_weight[i]=weight[i] - (tmp_weight[i]/(nupdates[0]+1))
    print(nupdates[0])

#結果の計算
def evaluate(weight_vector):
    naiseki=0
    seikai=0
    instance=0
    for i in range(len(test_data)):
        test=test_data[i][1]
        label=test_data[i][0]
        naiseki=mult_fv(i,test,weight_vector)
        if (naiseki * label) > 0:
            seikai+=1
        instance+=1
        naiseki=0
    seikairitsu=(seikai/instance)*100
    return (seikai,instance,seikairitsu)

read_data=read_data(train_file,test_file)
max_index=int(read_data[1])

if __name__=="__main__":
    parser=OptionParser()
    parser.add_option
    weight=[0]*(max_index+1)
    tmp_weight=[0]*(max_index+1)
    ave_weight=[0]*(max_index+1)
    weight_vector_2=[0]*(max_index+1)
    train_data=read_data[0]
    test_data=read_data[2]
    nupdates=[0]*(max_index+1)
    for r in range(int(sys.argv[3])):
        update_weight()
    averaged_weight()
    for i in range(len(weight_vector_2)):
        weight_vector_2[i]=weight_vector_2[i]/(nupdates[0]+1)
    if sys.argv[7]==str(1):
        print(evaluate(ave_weight))
    else:
        print(evaluate(weight))

#print(weight[0:5])
#print(tmp_weight[0:50])

#hikaku_list=[0]*(max_index+1)
#for i in range(len(ave_weight)):
#    hikaku_list[i]=ave_weight[i]-weight_vector_2[i]    

#print(ave_weight[0:50])
#print(weight_vector_2[0:50])
#print(hikaku_list[0:50])
