def bsearch(v,L):
    l=0
    r=len(L)-1
    while(l<=r):
        m=(l+r)//2
        if(v==L[m]):
            return m
        elif(v<L[m]):
            r=m-1
        else:
            l=m+1
    return -1

def bsearchMin(v,L):
    l=0
    r=len(L)-1
    while(l<r):  #因为下面是r=m，而不是-1的关系，当l==r时，说明此时只有一个元素，如果这个k<=这个元素，
                  #就只会进入到else分支，这样r赋值m 也就是等于l 循环一直下去
        m=(l+r)//2
        if(v>L[m]):
            l=m+1
        else:   #和中间值判断，如果是小于和等于还要继续在左边搜索
            r=m
    return l if(v==L[l]) else -1

def bsearchMax(v,L):
    l=0
    r=len(L)-1
    while(l<r):
        m=(l+r+1)//2  #关键，如果l和r相邻时,由于运算规则，m是等于l的，也就是较小的那个
                      #m=(l+r)//2, l和r相邻是 m=l 后面的赋值时l=m,l值没变，一直循环下去
        if(v<L[m]):
            r=m-1
        else:
            l=m
    return l if(v==L[l]) else -1

if __name__=='__main__':
    v=18
    L=[3,5,7,14,18,34,29]
    print(bsearchMin(v,L))