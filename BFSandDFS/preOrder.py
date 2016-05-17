import StudyCode.BFSandDFS.mytree
import StudyCode.BFSandDFS.mystack

def preorderTraversal(root):
    if root==None:
        return
    print(root.val)
    preorderTraversal(root.left)
    preorderTraversal(root.right)

def preorderStack1(root):
    if root==None:
        return
    mystack=StudyCode.BFSandDFS.mystack.Stack(10)
    mystack.push(root)
    while(not mystack.isempty()):
        node=mystack.pop()
        print(node.val)
        if(node.right!=None):
            mystack.push(node.right)
        if(node.left!=None):
            mystack.push(node.left)

def preorderStack2(root):
    if root==None:
        return
    mystack=StudyCode.BFSandDFS.mystack.Stack(10)
    node=root
    while(node!=None or not mystack.isempty()):
        #此时不需要获取栈顶的值，根据上一个node的情况做出判断
        while(node!=None):
            mystack.push(node)
            print(node.val)
            node=node.left
        #在node为空的时候就需要获取栈顶值进行判断了
        node=mystack.getTop()
        mystack.pop()
        node=node.right

if __name__=='__main__':
    binT=StudyCode.BFSandDFS.mytree.TreeNode('t')
    binA=StudyCode.BFSandDFS.mytree.TreeNode('a')
    binB=StudyCode.BFSandDFS.mytree.TreeNode('b')
    binC=StudyCode.BFSandDFS.mytree.TreeNode('c')
    binD=StudyCode.BFSandDFS.mytree.TreeNode('d')
    binE=StudyCode.BFSandDFS.mytree.TreeNode('e')
    binF=StudyCode.BFSandDFS.mytree.TreeNode('f')
    binG=StudyCode.BFSandDFS.mytree.TreeNode('g')
    binH=StudyCode.BFSandDFS.mytree.TreeNode('h')
    binT.addLeft(binA)
    binT.addRight(binB)
    binA.addLeft(binC)
    binA.addRight(binD)
    binB.addRight(binE)
    binD.addLeft(binF)
    binE.addLeft(binG)
    binE.addRight(binH)

    preorderStack2(binT)