# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        if root.left==None and root.right==None:
            return root.val==sum
        elif root.left==None:
            return self.hasPathSum(root.right,sum-root.val)
        elif root.right==None:
            return self.hasPathSum(root.left,sum-root.val)
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val) 

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
sum=23

c=Solution().hasPathSum(root,sum)

