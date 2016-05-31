# -*- coding: utf-8 -*-
from numpy import *
#load "iris.data" to workspace
traindata = loadtxt("testDecisionTree.data",delimiter = ',',usecols = (0,1,2,3),dtype = float)
trainlabel = loadtxt("testDecisionTree.data",delimiter = ',',usecols = (range(4,5)),dtype = str)
feaname = ["#0","#1","#2","#3"] # feature names of the 4 attributes (features)
feanamecopy = feaname[:]
#args = [0,0,0,0]
args = mean(traindata,axis = 0)


#calculate the entropy
from math import log
def calentropy(label):    #根据label计算熵
    n = label.size # the number of samples
    #print n
    count = {} #create dictionary "count"
    for curlabel in label:
        if curlabel not in count.keys():
            count[curlabel] = 0
        count[curlabel] += 1
    entropy = 0
    #print count
    for key in count:
        pxi = float(count[key])/n #notice transfering to float first
        entropy -= pxi*log(pxi,2)
    return entropy

#testcode:
#x = calentropy(trainlabel)


#split the dataset according to label "splitfea_idx"
def splitdata(oridata,splitfea_idx):  #根据最佳分割feature进行数据分割
    arg = args[splitfea_idx] #get the average over all dimensions
    idx_less = [] #create new list including data with feature less than pivot
    idx_greater = [] #includes entries with feature greater than pivot
    n = len(oridata)
    for idx in range(n):
        d = oridata[idx]
        if d[splitfea_idx] < arg:
            #add the newentry into newdata_less set
            idx_less.append(idx)
        else:
            idx_greater.append(idx)
    return idx_less,idx_greater

#testcode:2
#idx_less,idx_greater = splitdata(traindata,2)


#give the data and labels according to index
def idx2data(oridata,label,splitidx,fea_idx):
    idxl = splitidx[0] #split_less_indices
    idxg = splitidx[1] #split_greater_indices
    datal = []
    datag = []
    labell = []
    labelg = []
    for i in idxl:
        datal.append(append(oridata[i][:fea_idx],oridata[i][fea_idx+1:]))
    for i in idxg:
        datag.append(append(oridata[i][:fea_idx],oridata[i][fea_idx+1:]))
    labell = label[idxl]
    labelg = label[idxg]
    return datal,datag,labell,labelg
    

#select the best branch to split
def choosebest_splitnode(oridata,label):  #根据最大信息增益选择最佳分割feature
    n_fea = len(oridata[0])
    n = len(label)
    base_entropy = calentropy(label)
    best_gain = -1
    for fea_i in range(n_fea): #calculate entropy under each splitting feature
        cur_entropy = 0
        idxset_less,idxset_greater = splitdata(oridata,fea_i)
        prob_less = float(len(idxset_less))/n
        prob_greater = float(len(idxset_greater))/n
        
        #entropy(value|X) = \sum{p(xi)*entropy(value|X=xi)}
        cur_entropy += prob_less*calentropy(label[idxset_less])
        cur_entropy += prob_greater * calentropy(label[idxset_greater])
        
        info_gain = base_entropy - cur_entropy #notice gain is before minus after
        if(info_gain>best_gain):
            best_gain = info_gain
            best_idx = fea_i
    return best_idx  

#testcode:
#x = choosebest_splitnode(traindata,trainlabel)



#create the decision tree based on information gain
def buildtree(oridata, label,feanamecopy):
    if label.size==0: #if no samples belong to this branch
        return "NULL"
    print(len(label))
    listlabel = label.tolist()
    print(len(listlabel))
    #stop when all samples in this subset belongs to one class
    if listlabel.count(label[0])==label.size: #如果全是一种类型，则不需要分类就是label[0]类型
        return label[0]
        
    #return the majority of samples' label in this subset if no extra features avaliable
    print(feanamecopy)
    if len(feanamecopy)==0:
        cnt = {}
        for cur_l in label:
            if cur_l not in cnt.keys():
                cnt[cur_l] = 0
            cnt[cur_l] += 1
        maxx = -1 
        for keys in cnt:
            if maxx < cnt[keys]:
                maxx = cnt[keys]
                maxkey = keys
        return maxkey
    
    bestsplit_fea = choosebest_splitnode(oridata,label) #get the best splitting feature
    print(bestsplit_fea,len(oridata[0]))
    cur_feaname = feanamecopy[bestsplit_fea] # add the feature name to dictionary
    print(cur_feaname)
    nodedict = {cur_feaname:{}}
    #print(nodedict)
    del(feanamecopy[bestsplit_fea]) #delete current feature from feaname
    split_idx = splitdata(oridata,bestsplit_fea) #split_idx: the split index for both less and greater
    data_less,data_greater,label_less,label_greater = idx2data(oridata,label,split_idx,bestsplit_fea)
    
    #build the tree recursively, the left and right tree are the "<" and ">" branch, respectively
    now_feanamecopy=feanamecopy[:]
    nodedict[cur_feaname]["<"] = buildtree(data_less,label_less,now_feanamecopy)
    nodedict[cur_feaname][">"] = buildtree(data_greater,label_greater,now_feanamecopy)
    #print(nodedict)
    return nodedict
    
#testcode:
mytree = buildtree(traindata,trainlabel,feanamecopy)
print(mytree)

#classify a new sample
def classify(mytree,testdata):
    if type(mytree).__name__ != 'dict':
        return mytree
    fea_name = list(mytree.keys())[0] #get the name of first feature
    fea_idx = feaname.index(fea_name) #the index of feature 'fea_name'
    val = testdata[fea_idx]
    nextbranch = mytree[fea_name]
    
    #judge the current value > or < the pivot (average)
    if val>args[fea_idx]:
        nextbranch = nextbranch[">"]
    else:
        nextbranch = nextbranch["<"]
    return classify(nextbranch,testdata)

#testcode
tt = traindata[0]
x = classify(mytree,tt)
print(x)
