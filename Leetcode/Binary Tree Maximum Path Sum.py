# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxPathSum2(root):
            if not root:
                return 0
            return root.val+max(maxPathSum2(root.left),maxPathSum2(root.right),0)
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.val
        m1=maxPathSum2(root.left)
        m2=maxPathSum2(root.right)
        m=max(m1,m2,m1+m2,0)+root.val
        if root.left==None:
            return max(self.maxPathSum(root.right),m)
        if root.right==None:
            return max(self.maxPathSum(root.left),m)
        return max(self.maxPathSum(root.left),self.maxPathSum(root.right),m)

root=TreeNode(9)
root.left=TreeNode(6)
root.right=TreeNode(-3)
root.right.left=TreeNode(-6)
root.right.right=TreeNode(2)
root.right.right.left=TreeNode(2)
root.right.right.left.left=TreeNode(-6)
root.right.right.left.right=TreeNode(-6)


c=Solution().maxPathSum(root)

