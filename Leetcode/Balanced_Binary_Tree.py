# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def treedepth(root):
            if root:
                return 1+max(treedepth(root.left),treedepth(root.right))
            return 0
        if not root:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.left):
            return abs(treedepth(root.left)-treedepth(root.right))<=1
        return False

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

c=Solution().isBalanced(root)