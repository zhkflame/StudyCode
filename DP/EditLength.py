def getEditLth(var_str,target):   #target表示目标串，var_str表示需要变成目标串的字符串
    lenV=len(var_str)
    lenT=len(target)
    matrix=[[0 for i in range(lenT+1)] for j in range(lenV+1)]
    '''
    for i in range(lenT+1):
        matrix[0][i]=i
    for j in range(lenV+1):
        matrix[j][0]=j
    for i in range(1,lenV+1,1):
        for j in range(1,lenT+1,1):
            matrix[i][j]=min(matrix[i-1][j-1] if(var_str[i-1]==target[j-1]) else matrix[i-1][j-1]+1,
                             matrix[i-1][j]+1,
                             matrix[i][j-1]+1)
    '''
    for i in range(lenV+1):
        for j in range(lenT+1):
            if(i==0):
                matrix[i][j]=j
            elif(j==0):
                matrix[i][j]=i
            else:
                matrix[i][j]=min(matrix[i-1][j-1] if(var_str[i-1]==target[j-1]) else matrix[i-1][j-1]+1,
                             matrix[i-1][j]+1,
                             matrix[i][j-1]+1)
        #print(matrix[i])
    #print(matrix[lenV])
    return matrix[lenV][lenT]


def getEditLth2(var_str,target):
    lenV=len(var_str)
    lenT=len(target)
    matrix=[i for i in range(lenT+1)]
    #print(matrix)
    leftup=matrix[0]  #斜上的值
    #print(matrix)

    for i in range(1,lenV+1,1):
        for j in range(0,lenT+1,1):
            if(j==0):
                leftup=matrix[j]
                matrix[j]=i
            else:
                temp=matrix[j]
                matrix[j]=min(leftup if(var_str[i-1]==target[j-1])else leftup+1,
                                matrix[j-1]+1,
                                matrix[j]+1)
                leftup=temp
    return matrix[lenT]


    '''下面是空间复杂度降维的方法，正确可用
    for i in range(lenV+1):
        for j in range(lenT+1):
            if(i==0):
                matrix[j]=j
            elif(j==0):
                leftup=matrix[j]   #在每行开始的时候，保存的leftup是第一个值，表示要处理的左上角的值
                matrix[j]=i        #此时需要本行的第一个值
            else:
                temp=matrix[j]     #在更新当前值之前，需要先暂存一下，要不然后面赋值就没了
                matrix[j]=min(leftup if(var_str[i-1]==target[j-1]) else leftup+1,
                             matrix[j]+1,
                             matrix[j-1]+1)
                leftup=temp
    return matrix[lenT]
    '''




a='b'
b=''
print(getEditLth2(a,b))