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
        def maxSum(root):
            if root:
                m1=maxSum(root.left)
                m2=maxSum(root.right)
                maxs=max(m1,m2,0)+root.val
                self.maxv=max(self.maxv,maxs,m1+m2+root.val)
                return maxs
            else:
                return 0
        self.maxv=root.val
        maxSum(root)
        return self.maxv

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(4)
c=Solution().maxPathSum(root)
                    

