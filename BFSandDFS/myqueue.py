class Queue():
    def __init__(self,size):
        self.queue=[0 for i in range(size)]
        self.max=size
        self.size=0     #size和__front用来控制插入队尾的元素。
        self.__front=0  #__front表示队列的起始位置，入队时它不变，只是改变size,出队时改变__front的值

    def push(self,ele):
        if self.isfull():
            print("the queue is full now")
        else:
            self.queue[(self.__front+self.size)%self.max]=ele
            print((self.__front+self.size)%self.max,":",self.queue[(self.__front+self.size)%self.max])
            self.size=self.size+1
    def pop(self):
        if self.isempty():
            print("the queue is empty")
        else:
            temp=self.__front
            self.__front=(self.__front+1)%self.max
            self.size=self.size-1
            return self.queue[temp]

    def isfull(self):
        return self.size==self.max

    def isempty(self):
        return self.size==0

a=Queue(5)
a.push('a')
a.push('b')
a.push('c')
a.push('d')
a.push('2')
a.push('t')
for i in range(a.size):
    print(a.queue[i])
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
