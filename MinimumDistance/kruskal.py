def kruskal(graph,distance):
    lenG=len(graph)
    maskG=[i for i in range(lenG)]
    num=lenG*(lenG-1)//2
    edge=[]
    for i in range(lenG-1):
        for j in range(i+1,lenG,1):
            edge.append([graph[i][j],i,j])
    quicksort(edge,0,num-1)
    sum=0
    count=0
    for i in range(num): #利用递归函数求两端点的根节点x,y
        #x=getroot(maskG,edge[i][1])
        #y=getroot(maskG,edge[i][2])
        #利用非递归来求两端点的根节点x,y
        x=edge[i][1]
        while x!=maskG[x]:
            x=maskG[x]
        y=edge[i][2]
        while y!=maskG[y]:
            y=maskG[y]
        if(x!=y):
            sum=sum+edge[i][0]
            maskG[y]=x                  #将其中一个点的根节点更新为另一个点的根节点，使其连通有相同根节点
            count=count+1
    if(count<lenG-1):
        sum=0
    print(sum)

#找到一条边的一个节点的根节点，然后判断两个端点的根节点是否相同，如果相同，成环了，不可加入
#初始状态节点本身就是自己的根节点，在加入集合的过程中，更改尾节点的根节点为首节点的根节点
#只要节点本身与其根节点不同，就会不断的继续往下找，知道找到相同为止。
def getroot(maskG,node):
    if maskG[node]==node:
        return node
    else:
        return getroot(maskG,maskG[node])

#利用快速排序对边进行排序
def quicksort(edge,l,r):
    lenE=len(edge)
    if l>=r:
        return
    i,j=l,r
    temp=edge[l]
    while(i<j):
        while(i<j and edge[j][0]>temp[0]):
            j=j-1
        edge[i]=edge[j]
        while(i<j and edge[i][0]<=temp[0]):
            i=i+1
        edge[j]=edge[i]
    edge[i]=temp
    quicksort(edge,l,i-1)
    quicksort(edge,i+1,r)
    return edge

if __name__=="__main__":
    #edge=[[32,'0','1'],[23,'0','3'],[27,'1','4'],[14,'4','5']]
    #quicksort(edge,0,len(edge)-1)
    graph=[[0,2,5,14,999],
           [2,0,999,4,999],
           [5,999,0,999,4],
           [14,4,999,0,2],
           [999,999,4,2,0]]
    kruskal(graph,distance=[])