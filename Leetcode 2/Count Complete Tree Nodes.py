# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
        return 0

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.right=TreeNode(4)
c=Solution().countNodes(root)