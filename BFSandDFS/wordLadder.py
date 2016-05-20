import queue

def ladderLength(beginWord, endWord, wordList):
    if(beginWord==endWord):
        return 1
    LenL,pre={},{}
    LenL[beginWord]=1   #记录到每个词汇用的步长
    pre[beginWord]=''   #记录每个词的前一词汇
    myqueue=queue.Queue()
    myqueue.put(beginWord)
    wordList.add(endWord)  #将要比较的词放入词典中
    while(not myqueue.empty()):     #BFS框架开始，即队列不为空
        word=myqueue.get()          #取队首元素，
        step=LenL[word]+1
        for i in range(len(word)):                    #下面两部是进行可能的变换，寻找符合条件的元素加入队列
            for asc in range(ord('a'),ord('z')+1 ,1):
                str=chr(asc)
                if(word[i]!=str):         #判断单个字符串是否与待比较的词对应的字符相同，不同就可以变换，判断是否满足条件
                    temp=list(word)       #不能直接对str[i]修改，先转换成list,在修改，在变回来
                    temp[i]=str
                    word_temp=''.join(temp)
                    if((word_temp in wordList) and (not word_temp in LenL)):  #如果变换后的词在给出的字典里，并且每出现过则加入队列
                        pre[word_temp]=word
                        if(word_temp==endWord):
                            print("success")
                            while(pre[word_temp]!=''):
                                print(pre[word_temp])
                                word_temp=pre[word_temp]
                            return step
                        myqueue.put(word_temp)
                        LenL[word_temp]=step
                        print(word_temp,step)

    return 0

start='abcd'
end='defc'
LenL=set(("aecd","abfd","decd","defd","abfc","aefc"))
print(ladderLength(start,end,LenL))
