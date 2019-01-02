# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def preorder(root,k):
            if root:
                if k-root.val in self.d:
                    return True
                self.d[root.val]=1
                return preorder(root.left,k) or preorder(root.right,k)
            return False
        self.d=dict()
        return preorder(root,k)

root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(6)

c=Solution().findTarget(root,9)