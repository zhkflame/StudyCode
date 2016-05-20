#用类来解决问题，而不是函数
class queen(object):
    m_MainDiagonal=[]
    m_MinorDiagonal=[]
    m_Answer=[]
    m_Colomn=[]
    m_Queen=0

    def __init__(self,size):
        self.m_Queen=size
        self.m_Colomn=[False for i in range(size)]
        self.m_MainDiagonal=[False for i in range(2*size-1)]
        self.m_MinorDiagonal=[False for i in range(2*size-1)]
        #print(len(self.m_Colomn),len(self.m_MainDiagonal),len(self.m_MinorDiagonal))

    def CalQueen(self,path,row):
        if row==self.m_Queen:
            temp=path[:]  #不能直接appendpath，列表中存的是指针，值回变，需要转存在添加进去
            self.m_Answer.append(temp)
            return True
        for col in range(self.m_Queen):
            if self.CanLay(row,col):
                path[row]=col
                self.m_Colomn[col]=True
                self.m_MinorDiagonal[row+col]=True
                self.m_MainDiagonal[row-col+self.m_Queen-1]=True


                #用于找到所有解的情况
                self.CalQueen(path,row+1)
                self.m_Colomn[col]=False
                self.m_MinorDiagonal[row+col]=False
                self.m_MainDiagonal[row-col+self.m_Queen-1]=False


                #回溯,如果路径不正确，需要重新改回初值
                '''
                if not self.CalQueen(path,row+1):
                    self.m_Colomn[col]=False
                    self.m_MinorDiagonal[row+col]=False
                    self.m_MainDiagonal[row-col+self.m_Queen-1]=False
                '''
        return False




    def CanLay(self,row,col):
        return not self.m_Colomn[col] and \
               not self.m_MainDiagonal[row -col+self.m_Queen-1] and \
               not self.m_MinorDiagonal[row+col]

    def Queen(self):
        path=[0 for i in range(self.m_Queen)]
        #print(path)
        self.CalQueen(path,0)

    def PrintAnswer(self):
        print(self.m_Answer)

if __name__=="__main__":
    myQueen=queen(8)
    myQueen.Queen()
    myQueen.PrintAnswer()
