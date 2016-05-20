def sunday(t_str,p_str):
    lenT=len(t_str)
    lenP=len(p_str)
    moveLengh=[]   #用来存放遇到每一个字符所需移动的距离，默认是lenP+1
    for i in range(256):
        moveLengh.append(lenP+1)
    for i in range(lenP):    #如果是模式串中出现的字符，则需要根据出现在模式串中的位置来移动，如果多次出现，根据最右的位置移动
        #print(ord(p_str[i]))
        moveLengh[ord(p_str[i])]=lenP-i
    m=lenT-lenP+1
    i=0
    while(i<m):  #i==m的时候t_str剩余的元素就不够lenP了

        if(t_str[i]==p_str[0]):
            x=i+1
            y=1
            while(y<lenP and t_str[x]==p_str[y]):
                x,y=x+1,y+1
            if(y==lenP):
                return i
            if(t_str[x]!=p_str[y]):
                #print(t_str[i+lenP])
                #print(ord(t_str[i+lenP]))

                if(i+lenP<lenT):
                    i=i+moveLengh[ord(t_str[i+lenP])]
                else:
                    return -1
        else:
            i=i+1

a='mississippi'
b='sippj'
print(sunday(a,b))
