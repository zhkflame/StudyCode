def floyd(graph,distance):
    lenG=len(graph)
    #给distance赋初值
    for i in range(lenG):
            for j in range(lenG):
                distance[i][j]=graph[i][j]

    #k要从第0个查到第lenG-1个
    for k in range(lenG):
        #最开始不插入点，distance=graph，然后插入第一个点，用这个点将i,j两点分开，判断i到j距离 与i到k和k到j的距离和
        for i in range(lenG):
            for j in range(lenG):
                    #不断的用第k个点去分隔i,j,并更新最新最短距离
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
            print(distance[i])
        print("- - - - - - - - - - - - - - - -")
    return distance

if __name__=="__main__":
    graph=[[0   ,17  ,9999,9999,16  ,   1],
           [17  ,0   ,6   ,5   ,9999,  11],
           [9999,6   ,0   ,10  ,9999,9999],
           [9999,5   ,10  ,0   ,4   ,  14],
           [16  ,9999,9999,4   ,0   ,  33],
           [1   ,11  ,9999,14  ,33  ,   0]]
    distance=[[9999 for i in range(len(graph))] for j in range(len(graph))]
    print(floyd(graph,distance))