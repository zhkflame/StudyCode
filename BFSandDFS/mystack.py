class Stack():
    def __init__(self,size):
        self.size=size
        self.__stack=[]
        self.__top=-1

    def push(self,ele):
        if self.isfull():
            print("out of range")
        else:
            self.__stack.append(ele)
            self.__top=self.__top+1

    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.__top=self.__top-1
            return self.__stack.pop()
    def getTop(self):
        if self.__top!=-1:
            return self.__stack[self.__top]

    def isfull(self):
        return self.__top+1==self.size

    def isempty(self):
        return self.__top==-1
if __name__=='__main__':
    a=Stack(10)
    a.push('b')
    a.push('c')
    print(a.getTop())
    print(a.pop())