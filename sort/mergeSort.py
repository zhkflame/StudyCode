‘’‘tst'''
'''归并排序用的是递归，需要申请一个新的空间，并且需要把新空间已有序的区间复制到元数组，使得继续归并
'''
def mergeAdjust(L,L_m,start,mid,end):
    i,j,k=start,mid+1,start
    while(i<=mid and j<=end):
        if(L[i]<=L[j]):
            L_m[k]=L[i]
            i,k=i+1,k+1
        else:
            L_m[k]=L[j]
            j,k=j+1,k+1
    while(i<=mid):
        L_m[k]=L[i]
        i,k=i+1,k+1
    while(j<=end):
        L_m[k]=L[j]
        j,k=j+1,k+1
    for i in range(0,end+1,1):
        L[i]=L_m[i]
    '''
    不能采用不申请空间交换的方式，因为交换之后不能保证交换后的顺序正确
    while(i<=mid and j<=end):
        if(L[i]<=L[j]):
            i=i+1
        else:
            L[i],L[j]=L[j],L[i]
            j=j+1
    while(i<=mid):
        L_m[k]=L[i]
        i,k=i+1,k+1
    while(j<=end):
        L_m[k]=L[j]
        j,k=j+1,k+1
    for i in range(0,end+1,1):
        L[i]=L_m[i]
    '''
def mergeSort(L,L_m,start,end):
    if(start<end):
        mid=(start+end)//2
        mergeSort(L,L_m,start,mid)
        mergeSort(L,L_m,mid+1,end)
        mergeAdjust(L,L_m,start,mid,end)
       # L=L_m[:]

if __name__=="__main__":
    a=[3,67,123,71,72,1101,2,4,45,21,1,34,7,28,121]
    a_m=a[:]
    mergeSort(a,a_m,0,len(a)-1)
    print(a_m)