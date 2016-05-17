def prime(graph,point,distance):
    lenG=len(graph)
    isvisit=[False for j in range(len(graph))]
    isvisit[point]=True
    sum=0
    '''distance的定义变了,distance不是到point的最短距离，是从point点开始，向外扩展，
    每次选择的最小距离，不一定是Point到下一个点的距离'''
    for i in range(lenG):   #给记录距离的数组赋初值
        distance[i]=graph[point][i]
    for i in range(lenG): #不断的循环，找最小距离的点，知道所有点都被搜过，isvisit全为Ture
        k=9999      #记录此次找到最小距离结点的序号
        min=9999
        for j in range(lenG):  #找到当前距离中的最小值
            if(isvisit[j]==False and distance[j]<min):
                min=distance[j]
                k=j
        if(min==9999): #min=9999说明没有在更新值了，已经更新完毕，退出循环
            break
        isvisit[k]=True
        #更新到当前找到最小距离
        sum=sum+min
        #以当前找到的最小的距离点去更新到达其他点的距离
        for j in range(lenG):
            if(isvisit[j]==False and graph[k][j]<distance[j]):
                distance[j]=graph[k][j]
    return sum

if __name__=="__main__":
    graph=[[0   ,17  ,9999,9999,16  ,   1],
           [17  ,0   ,6   ,5   ,9999,  11],
           [9999,6   ,0   ,10  ,9999,9999],
           [9999,5   ,10  ,0   ,4   ,  14],
           [16  ,9999,9999,4   ,0   ,  33],
           [1   ,11  ,9999,14  ,33  ,   0]]
    distance=[9999 for j in range(len(graph))]
    print(prime(graph,1,distance))