# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def Depth(self,root,depth):
            depth+=1
            if root.left==None and root.right==None:
                return depth
            elif root.left==None:
                return Depth(self,root.right,depth)
            elif root.right==None:
                return Depth(self,root.left,depth)
            else:
                return min(Depth(self,root.left,depth),Depth(self,root.right,depth))
        if root:
            return Depth(self,root,0)
        else:
            return 0

root=TreeNode(0)
#root.left=TreeNode(1)
#root.left.left=TreeNode(2)
#root.right=TreeNode(3)
#root.right.right=TreeNode(4)

c=Solution().minDepth(root)

