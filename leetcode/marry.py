def marry(man,woman,resultMan):
    lenM=len(man)
    lenW=len(woman)
    if lenM!=lenW:
        print("no equel")
        return
    if lenM<=0:
        return 0
    resultMan=[-1 for i in range(lenM)]  #男生找了几号女生，默认是-1没有
    resultWoman=[-1 for i in range(lenW)] #女生找了几号男生
    manIndex=[0 for i in range(lenM)]  #男生被拒绝的次数
    wrank=[[0 for j in range(lenW)]for i in range(lenM)]  #初始化每个女生喜欢男生的顺序
    for i in range(lenW):
        for j in range(lenM):
            wrank[i][woman[i][j]]=j
            #反转下标和内容，表示女儿对男生的排名
    bSingle=False   #记录是否还有单身狗
    while not bSingle:   #如果有单身狗
        bSingle=True   #尚未发现单身狗
        for i in range(lenM):
            if resultMan[i]!=-1:
                continue
            bSingle=False  #发现单身狗
            j=manIndex[i]  #找到目前表白到第几个女生
            manIndex[i]=manIndex[i]+1
            w=man[i][j]  #男孩i第j个喜欢的女孩
            m=resultWoman[w]  #女孩的当前那男友
            if m==-1 or wrank[w][i]<wrank[w][m]:
                resultMan[i]=w
                resultWoman[w]=i
                if m!=-1:
                    resultMan[m]=-1

    return resultMan

def Validate(man,woman,match):
    return


if __name__=="__main__":
    man=[[2,3,1,0],
         [2,1,3,0],
         [0,2,3,1],
         [1,3,2,0]]
    woman=[[0,3,2,1],
           [0,1,2,3],
           [0,2,3,1],
           [1,0,3,2]]
    resultMan=[]

    print(marry(man,woman,resultMan))
    Validate(man,woman,resultMan)