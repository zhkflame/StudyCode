import StudyCode.BFSandDFS.mytree
import StudyCode.BFSandDFS.mystack

def inorderTraversal(root):
    if root==None:
        return
    inorderTraversal(root.left)
    print(root.val)
    inorderTraversal(root.right)

#第一种方法，利用一个另一个变量保存当前结点访问的次数，初始为0，该访问左子树+1，访问自身，然后出栈访问右子树
def inorderStack1(root):
    if root==None:
        return
    mystack=StudyCode.BFSandDFS.mystack.Stack(10)
    mystack.push([root,0])
    while((not mystack.isempty())):
        node=mystack.getTop()
        if node[1]==0:
            node[1]=node[1]+1
            if(node[0].left!=None):
                mystack.push([node[0].left,0])
        else:
            print(node[0].val)
            mystack.pop()
            if(node[0].right!=None):
                mystack.push([node[0].right,0])


def inorderStack2(root):
    if root==None:
        return
    mystack=StudyCode.BFSandDFS.mystack.Stack(10)
    node=root
    while(node!=None or not mystack.isempty()):
        #这种方法在进入循环的时候没有node=mystack.getTop()过程，是接着上一部的node值来继续判断的
        while(node!=None):
            mystack.push(node)
            node=node.left
        node=mystack.getTop()
        print(node.val)
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

    inorderStack2(binT)