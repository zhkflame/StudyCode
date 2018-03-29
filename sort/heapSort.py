#假设一个堆除了顶点以外是满足堆的定义，那么需要调整顶点及先其子孙节点满足堆的性质
#start是开始的下标，end是结束的下标
def adjustToHeap(L,start,end):
    if(start>end):
        return -1
    i=start
    '''错误示例
    if((2*i+1)<=end and L[2*i+1]>L[i]):
        L[2*i+1],L[i]=L[i],L[2*i+1]
        if((2*i+2)>end or ((2*i+2)<=end and L[2*i+2]<=L[i])):
            adjustToHeap(L,2*i+1,end)
       # adjustToHeap(L,2*i+1,end)
    if((2*i+2)<=end and L[2*i+2]>L[i]):
        L[2*i+2],L[i]=L[i],L[2*i+2]   #问题出现了，因为有可能换两次，就必然首先和左孩子换，在和有孩子换，这样
        adjustToHeap(L,2*i+2,end)     #就会沿着右孩子的路径往下走，左孩子就不走了
    '''

    ''' #用了递归的正确的版本 递归的判断条件在初始判断条件，如果不满足会return
    if(2*i+1<=end):  #进到每一个函数的判断条件就是他的左孩子要小于等于终结点
        if(2*i+2<=end and L[2*i+2]>L[2*i+1] and L[2*i+2]>L[i]): #如果有右节点，并且大于左节点还大于父节点，那么换
            L[2*i+2],L[i]=L[i],L[2*i+2]
            adjustToHeap(L,2*i+2,end)
        elif(L[2*i+1]>L[i]):
            L[2*i+1],L[i]=L[i],L[2*i+1]
            adjustToHeap(L,2*i+1,end)
    '''
    #改用循环
    max=i
    while(i<=end):  #这一步可以没有，但是可以预防函数传入参数的问题
        if(2*i+1<=end): # 判断两个孩子谁大谁小
            if(2*i+2<=end and L[2*i+2]>L[2*i+1]):
                max=2*i+2
            else:
                max=2*i+1
            if(L[max]>L[i]):  #判断父节点与较大孩子的大小
                L[max],L[i]=L[i],L[max]
                i=max
            else:
                return
        else:
            return



def HeapSort(L,len):
    #建堆  关键问题是边界，从哪个开始，哪个结束
    #len-1是数组最大的下标，他的父节点序号是（len-1-1）//2，需要调整到最后一个根节点就是0，
    #根据range左闭右开的性质，那么右侧如果是0就不包括0了，是-1才能包括0.
    for i in range((len-2)//2,-1,-1):
        adjustToHeap(L,i,len-1)
    #调整堆
    for i in range(len-1,0,-1):
        L[i],L[0]=L[0],L[i]
        adjustToHeap(L,0,i-1)
    return  L

if __name__=="__main__":
    a=[3,67,123,71,72,1101,2,4,45,21,1,34,7,28,121]
    b=[18,9,7]
    print(a)
    print(HeapSort(a,len(a)))

