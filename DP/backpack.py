#值小于等于maxHeavy的最大价值
def getDP(heavy,value,maxHeavy):
    lenH=len(heavy)
    lenV=len(value)
    matrix=[[0 for i in range(maxHeavy+1)] for j in range(lenH+1)]
    for i in range(1,lenH+1,1):
        for j in range(1,maxHeavy+1,1):
            if j>=heavy[i-1]:
                #判断的时候只与i的值相关，与j的值无关
                matrix[i][j]=max(matrix[i-1][j],matrix[i-1][j-heavy[i-1]]+value[i-1])
                print(value[i-1])
            else:
                matrix[i][j]=matrix[i-1][j]

    return matrix[lenH][maxHeavy]

def getDP2(heavy,value,maxHeavy):
    lenH=len(heavy)
    lenV=len(value)
    matrix=[0 for i in range(maxHeavy+1)]
    for i in range(1,lenH+1,1):
        #j是倒叙的，因为更新当前的j需要上一行的值，包括matrix[i-1][j],matrix[i-1][j-heavy[i-1]]，后一项在前面，
        #如果从前往后更新，则获取不到之前的值了
        for j in range(maxHeavy,heavy[i-1]-1,-1):
            matrix[j]=max(matrix[j],matrix[j-heavy[i-1]]+value[i-1])
    return matrix[maxHeavy]

#值刚好为maxHeavy的最大价值
def getDP3(heavy,value,maxHeavy):
    lenH=len(heavy)
    lenV=len(value)
    matrix=[-9999999 for i in range(maxHeavy+1)]
    matrix[0]=0
    for i in range(1,lenH+1,1):
        print(heavy[i-1],"------")
        #初值都是最小，[0]是0，只有当j的值存在于heavy数组中，或是数组中的数的和时，才会更新matrix[j]
        for j in range(maxHeavy,heavy[i-1]-1,-1):
            matrix[j]=max(matrix[j],matrix[j-heavy[i-1]]+value[i-1])
            if(matrix[j]>=0):
                print(j,matrix[j])
    return matrix[maxHeavy]

def getDP4(heavy,value,maxValue):
    lenH=len(heavy)
    lenV=len(value)
    matrix=[9999999 for i in range(maxValue+1)]
    matrix[0]=0
    for i in range(1,lenV+1,1):
        #初值都是最大，[0]是0，只有当j的值存在于value数组中，或是数组中的数的和时，才会更新matrix[j]
        for j in range(maxValue,value[i-1]-1,-1):
            matrix[j]=min(matrix[j],matrix[j-value[i-1]]+heavy[i-1])
    return matrix[maxValue]



things={23:100,15:75,34:110,7:26,45:180,30:80,60:170,10:31}
heavy=[23,15,34,7,45,30,60,10]
value=[100,75,110,26,180,80,170,31]
maxHeavy=100
maxValue=180
#print(getDP3(heavy,value,maxHeavy))
print(getDP4(heavy,value,maxValue))
