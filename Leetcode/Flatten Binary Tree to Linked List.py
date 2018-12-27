# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def preorder(root,List):
            if root:
                List.append(root.val)
                preorder(root.left,List)
                preorder(root.right,List)
        if not root:
            return None
        List=[]
        preorder(root,List)
        n=len(List)
        p=root
        p.left=None
        for i in range(1,n):
            p.right=TreeNode(List[i])
            p=p.right
        

root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)          
root.right=TreeNode(5)
root.right.right=TreeNode(6)

Solution().flatten(root)