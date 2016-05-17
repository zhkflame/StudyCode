def maxSubArray(L,n,start):  #start表示每次递归的起始位置
    if(n==1):
        return L[start]
        #return L[0]
    mid=n>>1
    #以mid二分，左边有0-mid-1共mid项，右边有n-mid项
    answer=max(maxSubArray(L,mid,start),maxSubArray(L,n-mid,start+mid))  #第一种情况，在左边或右边的最大和
    #print(answer)
    #第二种情况，包含中心位置的最大和
    now=L[start+mid-1]   #now表示中间位置的值
    may=now         #may表示包含当前位置，并向前后向后移动值得最大值
    for i in range(start+mid-2,start-1,-1):
        now=now+L[i]
        may=max(may,now)
    now=may    #now为从左边搜索之后的最大值
    for i in range(start+mid,start+n,1):
        now=now+L[i]
        may=max(may,now)
    return max(answer,may)

def maxArrUseDP(L,n):  #需要求以每一个元素结尾的最大连续和
    matrix=L[:]
    max=matrix[0]
    for i in range(1,n,1):
        if(L[i]+matrix[i-1]>matrix[i]):
            matrix[i]=matrix[i-1]+L[i]
        if(max<matrix[i]):
            max=matrix[i]
    return max

def maxArrUseDP2(L,n):  #空间复杂度为O(1)
    matrix=L[0]  #matrix保存需要比较的前一个元素的最大和，然后根据与当前元素加和后的比较条件来
    max=L[0]
    for i in range(1,n,1):
        if(L[i]+matrix>L[i]):
            matrix=matrix+L[i]
        else:
            matrix=L[i]
        if(max<matrix):
            max=matrix
    return max


a=[-2,1]
print(maxArrUseDP2(a,len(a)))