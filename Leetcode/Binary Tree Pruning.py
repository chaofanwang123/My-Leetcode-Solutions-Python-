# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if root.val==0 and root.left==None and root.right==None:
            return None
        return root

root=TreeNode(1)
root.left=TreeNode(0)
root.left.left=TreeNode(0)
root.left.right=TreeNode(0)
root.right=TreeNode(1)
root.right.left=TreeNode(0)
root.right.right=TreeNode(1)

c=Solution().pruneTree(root)