def quickSort(L,start,end):
    if(start<end):   #退出循环的条件
        l,r=start,end
        temp=L[start]
        while(l<r): #找到位置的条件边界
            ''' 这么写更符合逻辑，更规范，单多了两个判断，两个赋值
            while(l<r and temp<=L[r]):  #从右开始，找到第一个小于的
                r=r-1
            if(l<r):                      #此处应有判断，表示不是因为l==r退出循环的，赋值是有条件的
                L[l]=L[r]                   #左边的位置等于第一个r
                l=l+1
            while(l<r and temp>L[l]):   #从左开始，找到第一个大于的
                l=l+1
            if(l<r):
                L[r]=L[l]                   #右边的位置等于第一个l
                r=r-1
            '''
            #这么写更有效率，少了两个if判断
            while(l<r and temp<=L[r]):
                r=r-1
            L[l]=L[r]
            while(l<r and temp>L[l]):
                l=l+1
            L[r]=L[l]
        L[l]=temp
        quickSort(L,start,l-1)
        quickSort(L,l+1,end)
        #return L

if __name__=="__main__":
    a=[3,67,123,71,72,1101,2,4,45,21,1,34,7,28,121]
    quickSort(a,0,len(a)-1)
    print(a)