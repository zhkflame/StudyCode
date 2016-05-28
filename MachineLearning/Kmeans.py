from numpy import *
import operator

def k_means(data,k):
    m=len(data)
    n=len(data[0])
    cluster=[-1 for x in range(m)]   #所有样本
    cluster_center=[[]for x in range(k)]  #聚类的k个中心
    c_next=[[] for x in range(k)]  #下一轮聚类中心
    c_number=[0 for x in range(k)] #每个簇中样本的数目

    #随机选取簇中心
    i=0
    while i<k:
        j=random.randint(0,m-1)
        if is_similar(data[j],cluster_center):
            continue
        cluster_center[i]=data[j][:]
        c_next[i]=[0 for  x in range(n)]
        i+=1
    for times in range(40):
        for i in range(m):
            c=nearest(data[i],cluster_center)
            cluster[i]=c
            c_number[c]+=1
            add(c_next[c],data[i])   #求第c簇的和
        for i in range(k):
            divide(c_next[i],c_number[i])  #求第i簇的均值
            c_number[i]=0   #重新置0
            cluster_center[i]=c_next[i][:]
            zero_list(c_next[i])  #把c_next置0
        print(times,cluster_center)
    return cluster


def is_similar(data,cluster_center):
    return False

def nearest(data,cluster_center):
    return

def zero_list(data):
    return
