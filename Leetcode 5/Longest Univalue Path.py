# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def path(root):
            if not root:
                return 0
            l=1
            r=1
            if root.left:
                m=path(root.left)
                l=m+1 if root.left.val==root.val else 1
            if root.right:
                n=path(root.right)
                r=n+1 if root.right.val==root.val else 1
            if root.left and root.right and root.left.val==root.right.val==root.val:
                self.max=max(self.max,l+r-1)
            max_v=max(l,r)
            self.max=max(self.max,max_v)
            return max_v
        self.max=1
        path(root)
        return self.max-1

