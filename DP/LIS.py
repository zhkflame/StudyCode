import StudyCode.DP.LCS
import StudyCode.sort.quickSort


def LISuseLCS(L):
    lenL=len(L)
    if(lenL<=0):
        return -1
    L2=L[:]
    StudyCode.sort.quickSort.quickSort(L, 0, lenL - 1)
    #return L
    return StudyCode.DP.LCS.LCS(L, L2)

def LIS(L):
    lenL=len(L)
    if(lenL<=0):
        return -1
    matrix=[1 for l in range(lenL)]  #用来记录以每个元素为结尾的递增字串有多长
    max=1   #记录最大值
    for i in range(lenL):  #从第二个遍历也可以
        for j in range(i):
            if(L[i]>L[j]):  #公式中的判断条件
                if(matrix[j]+1>matrix[i]):   #如果新值大于旧值需要更新
                    matrix[i]=matrix[j]+1    #赋值部分
        if(matrix[i]>max):
            max=matrix[i]
    print(matrix)
    return max

a=[0,56,1,5,3,5,60,45]
print(LIS(a))