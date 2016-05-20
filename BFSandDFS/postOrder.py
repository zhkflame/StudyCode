import StudyCode.BFSandDFS.mytree
import StudyCode.BFSandDFS.mystack

def postorderTraversal(root):
    if root==None:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.val)

#第一种方法，利用一个另一个变量保存当前结点访问的次数，初始为0，该访问左子树+1，然后为1访问右子树，最后访问本身
def postorderStack1(root):
    if root==None:
        return
    mystack=StudyCode.BFSandDFS.mystack.Stack(10)
    mystack.push([root,0])
    while(not mystack.isempty()):
        node=mystack.getTop()
        if(node[1]==0):
            node[1]=node[1]+1
            if(node[0].left!=None):
                mystack.push([node[0].left,0])
        elif node[1]==1:
            node[1]=node[1]+1
            if(node[0].right!=None):
                mystack.push([node[0].right,0])
        else:
            print(node[0].val)
            mystack.pop()

def postorderStack2(root):
    if root==None:
        return
    mystack=StudyCode.BFSandDFS.mystack.Stack(10)
    mystack.push(root,)
    pre=None
    while(not mystack.isempty()):
        node=mystack.getTop()
        if((node.left==None and node.right==None)  #如果左右子树都为空，则可以访问当前结点并出栈
           or (pre!=None #如果不是都为空，则可能有一个为空，因为pre初始值为空，此时会存在有一个不为空，但进入循环的情况
               and (pre==node.left or pre==node.right))):  #后序遍历的特点：如果有孩子，则前序必为其中一个孩子
            print(node.val)
            mystack.pop()
        else:
            if node.right!=None:
                mystack.push(node.right)
            if node.left!=None:
                mystack.push(node.left)
        pre=node


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

    postorderStack2(binB)