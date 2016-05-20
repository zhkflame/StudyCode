def searchStr(t_str,p_str):
    lenT=len(t_str)
    lenP=len(p_str)
    if(lenT<lenP):
        return -1
    s,i,j=0,0,0
    print(lenT,lenP)
    while(s<=lenT-lenP):
        while(j<lenP and t_str[i]==p_str[j]):
            i,j=i+1,j+1
        if(j==lenP):
            return s
        if(t_str[i]!=p_str[j]):
            s=s+1
            i=s
            j=0
    return -1

T='ababcdabde'
P='abcdabd'
print(searchStr(T,P))