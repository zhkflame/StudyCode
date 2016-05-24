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
                for k in range(1,10,1):
                    self.chess[i][j]=k
                    '''
                    if(self.isValid(i,j) and self.sudoku()):
                        if not self.isSolve:
                            temp=copy.deepcopy(self.chess)
                            print(temp)
                            self.result.append(temp)
                            #下面用于只求一个解就返回
                            self.isSolve=True
                            return True
                    '''
                    if self.isValid(i,j):
                        if self.sudoku():
                            if not self.isSolve:
                                temp=copy.deepcopy(self.chess)
                                print(temp)

                                #下面一句用于求所有解
                                #self.result.append(temp)

                                #下面的用于找到一个解就返回，这个和上两个不同，不是利用步数开始就判断是否满足条件
                                self.isSolve=True
                                return True
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
    #多个解的数独
    chess3=[[6,0,8,1,0,2,0,7,0],
            [0,0,7,0,4,0,0,8,3],
            [0,0,9,3,0,0,1,0,0],
            [0,2,0,7,6,0,5,0,0],
            [0,0,4,0,9,0,0,1,0],
            [7,9,0,0,0,0,8,0,2],
            [4,0,5,0,3,0,7,0,8],
            [0,0,0,0,2,0,9,4,0],
            [0,0,2,5,0,4,0,6,0]]
    #无解的数独
    chess4=[[0,0,2,0,4,0,9,0,0],
            [3,6,0,1,0,2,0,4,7],
            [0,0,0,9,0,5,0,0,0],
            [1,5,0,0,3,0,0,9,2],
            [0,0,7,0,2,0,3,0,0],
            [8,2,0,0,7,0,0,6,1],
            [0,0,0,4,0,3,0,0,0],
            [6,7,0,2,0,8,0,5,4],
            [0,0,4,0,5,0,8,0,0]]
    mysudoku=sudoku(chess3)
    #print(mysudoku.chess)
    mysudoku.sudoku()
    mysudoku.printResult()
