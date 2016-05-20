def findSquare(go):
    lenG=go
    matrix=[[0 for i in range(lenG)] for j in range(lenG)]
    sum=0
    for i in range(1,lenG):
        for j in range(1,lenG):
            x,y=i,j
            while(x-1>=0 and y-1>=0):
                sum+=1
                x,y=x-1,y-1
    return sum

def findSquare2(go):
    lenG=go
    matrix=[0 for i in range(lenG)]
    sum=0
    for i in range(1,lenG):
        for j in range(1,lenG):
            if i==j:
                matrix[j]=matrix[j-1]+1
            else:
                matrix[j]=max(matrix[j-1],matrix[j])
            sum+=matrix[j]
    return sum

def findSquare3(go):
    lenG=go
    sum=0
    for i in range(1,lenG):
        for j in range(1,lenG):
            sum+=min(i,j)
    return sum

if __name__=="__main__":
    print(findSquare3(19))