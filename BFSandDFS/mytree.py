class TreeNode(object):
    def __init__(self,v=None):
        self.val=v
        self.right=None
        self.left=None
    def addLeft(self,ele):
        self.left=ele
    def addRight(self,ele):
        self.right=ele
    def setValue(self,v):
        self.val=v



if __name__=='__main__':
    binT=TreeNode('t')
    binA=TreeNode('a')
    binB=TreeNode('b')
    binC=TreeNode('c')
    binD=TreeNode('d')
    binE=TreeNode('e')
    binF=TreeNode('f')
    binG=TreeNode('g')
    binH=TreeNode('h')
    binT.addLeft(binA)
    binT.addRight(binB)
    binA.addLeft(binC)
    binA.addRight(binD)
    binB.addRight(binE)
    binD.addLeft(binF)
    binE.addLeft(binG)
    binE.addRight(binH)
    print(binT.value)
    print(binT.left.value)
    print(binT.right.value)
