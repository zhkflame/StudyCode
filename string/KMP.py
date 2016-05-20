def getNext(p_str):
    next=[]
    lenP=len(p_str)
    if(lenP<=2):
        return
    next.append(0)   #next数组的前两个元素为0
    next.append(0)   #因为第一个就不相等就要还从第一个比较，第二个不相等也要再从第一个比较
    k=0  # k用来表示当前位置对应的next数组中的值， k表示对应的值
    j=2 #j用来记录当前需要求解next的位置
    #for j in range(2,lenP,1):
    '''此处不适合用for，因为for一次循环之后变量要+1，while可以在内部控制变量变化
    j用来记录当前需要求解next的位置，即next[j]  j表示位置下表
    k用来表示当前位置对应的next数组中的值， k表示对应的值
    '''
    while(j<lenP):
        if(p_str[j-1]==p_str[k]):  #只要有一个值跟初始值相等，k就会增加的
            '''
            求当前位置的next值，需要判断前一元素是否与其(前一元素的）next值相等
            因为初始的时候都是应该返回起始元素（下标0的值）
            '''
            next.append(k+1)  #此处是用k+1来表示需要比较的位置，因为如果上面判断不相等，k会向前推进
            k=next[j]  #更新的是新添加的元素对应的next的值k,
            j=j+1
        else:
            if(k!=0):
                k=next[k]  #如果不等继续向前寻找
            else:   #如果向前寻找到==0了，则说明没有匹配的长度，需要从第一个比较
                next.append(0)
                j=j+1
    #print(next)
    return next
#没有考虑到为空的情况两个都为空的情况
def KMP(t_str,p_str):
    lenT=len(t_str)
    lenP=len(p_str)
    if(lenT<lenP):
        return -1
    if(lenP==0):
        return 0
    next=getNext(p_str)
    i,j=0,0
    for i in range(0,lenT,1):
        while(j>0 and t_str[i]!=p_str[j]):  #j>0还需要理解一下
            #如果此时j>0及模式串不是第一个元素，且他俩不想等，此时需要用next数组判断滑动距离
            #如果j==0,如果相等，则后面有判断依据，如果不等，则需要i+1，这么些没问题
            j=next[j]
        if(t_str[i]==p_str[j]):
            j=j+1;
        if(j==lenP):
            return i-lenP+1
    return -1

a='ababcdabde'
b='cdgcdeacdgcdgh'
print(getNext(b))
print(KMP(a,b))
