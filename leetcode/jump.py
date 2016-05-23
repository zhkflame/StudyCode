def jump(array):
    lenA=len(array)
    if lenA==0:
        return 0
    if array[0]>=lenA-1:
        return 1
    else:
        r=array[0]
        step=2
        max=array[0]
        i=1
        while(i<=r):
            if max<i+array[i]:
                max=i+array[i]
            if(max>=lenA-1):
                return step
            if i==r:
                i=i+1
                r=max
                step=step+1
            else:
                i=i+1


    return

if __name__=="__main__":
    a=[2,3,1,1,1,2,2,1,1]
    print(jump(a))


