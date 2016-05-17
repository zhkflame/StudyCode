import copy
class horse(object):
    ihorse=[-2,-2,-1,1,2,2,1,-1]
    jhorse=[-1,1,2,2,1,-1,-2,-2]
    chess=[]
    answer=[]
    row=0
    col=0
    count=0 #统计左上角为0的解


    def __init__(self,r,c):
        self.chess=[[0 for j in range(c)] for i in range(r)]
        self.chess[0][0]=1
        self.row=r
        self.col=c

    def canJump(self,chess,x,y):
        if(x<0 or x>=self.row or y<0 or y>=self.col):
            return False
        return chess[x][y]==0

    def jump(self,i,j,step):
        if step==self.row*self.col:
            temp=copy.deepcopy(self.chess)
            self.answer.append(temp)
            self.count+=1
            return True
        for k in range(8):
            iCur=i+self.ihorse[k]
            jCur=j+self.jhorse[k]
            if self.canJump(self.chess,iCur,jCur):
                self.chess[iCur][jCur]=step+1
                self.jump(iCur,jCur,self.chess[iCur][jCur])
                    #return True
                self.chess[iCur][jCur]=0
        return False

    def jump2(self,i,j,step):
         if step==self.row*self.col:
            temp=copy.deepcopy(self.chess)
            self.answer.append(temp)
            self.count+=1
            return True

         pHorse=[]
         nHorse=self.getHorseDirect(pHorse,i,j,step==(self.row*self.col-1))
         iCur,jCur=0,0
         nDirect=0
         for k in range(nHorse):
             nDirect=pHorse[k][0]
             iCur=i+self.ihorse[nDirect]
             jCur=j+self.jhorse[nDirect]
             self.chess[iCur][jCur]=step+1
             if self.jump2(iCur,jCur,step+1):
                 return True
             self.chess[iCur][jCur]=0
         return False

    #启发式搜索
    def getHorseDirect(self,pHorse,i,j,blast):
        nHorse=0
        iCur,jCur=0,0
        for k in range(8):
            iCur=i+self.ihorse[k]
            jCur=j+self.jhorse[k]
            if self.canJump(self.chess,iCur,jCur):
                if(blast):
                    pHorse.append([k,1])
                    nHorse+=1
                    break
                else:
                    nDirect=self.getNextStep(iCur,jCur)
                    if nDirect!=0:
                        pHorse.append([k,nDirect])
                        nHorse+=1
        if nHorse==0:
            return 0
        self.quicksort(pHorse,0,len(pHorse)-1)
        return nHorse


    def getNextStep(self,i,j):
        nDirect=0
        iCur,jCur=0,0
        for k in range(8):
            iCur=i+self.ihorse[k]
            jCur=j+self.jhorse[k]
            if self.canJump(self.chess,iCur,jCur):
                nDirect+=1
        return nDirect

    def printStep(self):
        print(self.count)
        print(self.answer)

    def quicksort(self,pHorse,l,r):
        lenE=len(pHorse)
        if l>=r:
            return
        i,j=l,r
        temp=pHorse[l]
        while(i<j):
            while(i<j and pHorse[j][1]>temp[1]):
                j=j-1
            pHorse[i]=pHorse[j]
            while(i<j and pHorse[i][1]<=temp[1]):
                i=i+1
            pHorse[j]=pHorse[i]
        pHorse[i]=temp
        self.quicksort(pHorse,l,i-1)
        self.quicksort(pHorse,i+1,r)
        return pHorse

if __name__=="__main__":
    myhorse=horse(8,10)
    myhorse.jump2(0,0,1)
    myhorse.printStep()

