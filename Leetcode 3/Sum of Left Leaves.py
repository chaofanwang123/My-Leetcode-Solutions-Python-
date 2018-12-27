# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(root):
            if root:
                if root.left and root.left.left==None and root.left.right==None:
                    self.value+=root.left.val
                preorder(root.left)
                preorder(root.right)
        self.value=0
        preorder(root)
        return self.value

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.left=TreeNode(2)
c=Solution().sumOfLeftLeaves(root)