# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            m1=dfs(root.left)
            m2=dfs(root.right)
            self.sum+=abs(m1-m2)
            return m1+m2+root.val
        
        if not root:
            return 0
        self.sum=0
        dfs(root)
        return self.sum

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)

c=Solution().findTilt(TreeNode(1))