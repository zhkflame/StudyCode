def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    lenT=len(haystack)
    lenP=len(needle)
    if(lenT<lenP and lenP==0):
        return -1
    if(lenT==0 and lenP==0):
        return 0
    next=[]
    next.append(0)
    next.append(0)
    k=0
    j=2
    while(j<lenP):
        if(needle[j-1]==needle[k]):
            next.append(next[j-1]+1)
            k=next[j]
            j=j+1
        else:
            if(k!=0):
             k=next[k]
            else:
                next.append(0)
                j=j+1
    i,j=0,0
    for i in range(0,lenT,1):
        while(j>0 and haystack[i]!=needle[j]):
            j=next[j]
        if(haystack[i]==needle[j]):
            j=j+1;
        if(j==lenP):
            return i-lenP+1

    return -1


a=''
b=''

print(strStr(a,b))