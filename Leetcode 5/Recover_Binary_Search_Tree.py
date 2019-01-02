# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inorder(root,List):
            if List[0]:
                return
            if root:
                inorder(root.left,List)
                if root.val<List[1].val:
                    if len(List)!=2:
                        tmp=root.val
                        root.val=List[2].val
                        List[2].val=tmp
                        List[0]=True
                        return
                    List.append(List[1])
                    List.append(root)
                List[1]=root 
                inorder(root.right,List)
        
        pre=TreeNode(float('-inf'))
        List=[]
        List.append(False)
        List.append(pre)
        inorder(root,List)
        if List[0]:
            return
        tmp=List[2].val
        List[2].val=List[3].val
        List[3].val=tmp
        return

def inorder2(root):
    if root:
        inorder2(root.left)
        print(root.val)
        inorder2(root.right)

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.right.left=TreeNode(2)
inorder2(root)
print('new inorder\n')

c=Solution().recoverTree(root)
inorder2(root)


