import copy
class sudoku(object):
    chess=[]
    result=[]
    isSolve=False

    def __init__(self,chess):
        self.chess=copy.deepcopy(chess)
        self.isSolve=False

    def sudoku(self):
        for i in range(9):
            for j in range(9):
                if self.chess[i][j]!=0:
                    continue
                for k in range(1,11,1):
                    self.chess[i][j]=k
                    if(self.isValid(i,j) and self.sudoku()):
                        if not self.isSolve:
                            temp=copy.deepcopy(self.chess)
                            print(temp)
                            self.result.append(temp)
                            self.isSolve=True
                            #return True
                    self.chess[i][j]=0
                return False
        return True


    def isValid(self,i,j):
        temp=self.chess[i][j]
        for k in range(9):
            if i!=k and temp==self.chess[k][j]:
                return False
            if j!=k and temp==self.chess[i][k]:
                return False
        iGrid=(i//3)*3   #求所在九宫格的有上角位置
        jGrid=(j//3)*3
        for iG in range(iGrid,iGrid+3,1):
            for jG in range(jGrid,jGrid+3,1):
                if iG==i and jG==j:
                    continue
                if temp==self.chess[iG][jG]:
                    return False
        return True

    def printResult(self):
        print(self.result)


if __name__=="__main__":
    chess=[[0,4,2,0,6,3,0,0,9],
           [6,0,0,0,1,0,0,0,5],
           [3,0,0,0,2,0,4,8,0],
           [1,0,0,5,0,2,6,0,8],
           [4,0,0,0,0,7,0,0,1],
           [9,0,5,6,0,0,0,0,7],
           [0,3,6,0,5,0,0,0,2],
           [2,0,0,0,7,0,0,0,4],
           [7,0,0,2,9,0,8,5,0]]
    mysudoku=sudoku(chess)
    print(mysudoku.chess)
    mysudoku.sudoku()
    mysudoku.printResult()
