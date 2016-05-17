def LCS(a_str,b_str):
    lenA=len(a_str)
    lenB=len(b_str)
    matrix = [[0 for col in range(lenB+1)] for row in range(lenA+1)]
    #b_matrix= [[[0,0] for col in range(lenB+1)] for row in range(lenA+1)]
    b_matrix=[]
    #b_matrix记录的是当前匹配元素的前一元素
    #a_str要是竖着的，也就是大循环
    for i in range(1,lenA+1,1):  #i是行号，大循环 而b_str的每个字符在每个行上
        for j in range(1,lenB+1,1):  #j是列号，小循环 而a_str的每个字符在每个列上
            if(a_str[i-1]==b_str[j-1]):
                matrix[i][j]=matrix[i-1][j-1]+1
                #b_matrix[i+1][j+1]=[i,j]
                b_matrix.append([i-1,j-1])
            else:
                #print(i,j+1,'   ',i+1,j)
                if(matrix[i-1][j]>=matrix[i][j-1]):
                    matrix[i][j]=matrix[i-1][j]
                   # b_matrix[i+1][j+1]=[i,j+1]
                else:
                    matrix[i][j]=matrix[i][j-1]
                  #  b_matrix[i+1][j+1]=[i+1,j]
    #return matrix[lenA][lenB]
       # print(b_matrix[i])
    #print(b_matrix)
    #print(matrix[lenA][lenB])
    return matrix[lenA][lenB]

def LCS2(a_str,b_str):
    lenA=len(a_str)
    lenB=len(b_str)
    matrix=[0 for i in range(lenB+1)]
    leftup=matrix[0]
    for i in range(1,lenA+1,1):
        for j in range(0,lenB+1,1):
            if(j==0):
                leftup=matrix[j]
                matrix[j]=0
            else:
                temp=matrix[j]
                if(a_str[i-1]==b_str[j-1]):
                    matrix[j]=leftup+1
                else:
                    matrix[j]=max(matrix[j],matrix[j-1])
                leftup=temp
    return matrix[lenB]

if __name__=="__main__":
    a='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    b='zabdkcacood'
    print(LCS2(a,b))