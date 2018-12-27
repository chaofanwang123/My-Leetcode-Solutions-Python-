# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetric(root1,root2):
            if root1==None:
                return root2==None
            if root2:
                if root1.val!=root2.val:
                    return False
                return symmetric(root1.left,root2.right) and symmetric(root1.right,root2.left)
            return False
        if not root:
            return True
        return symmetric(root.left,root.right)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(3)
root.right.right=TreeNode(4)

c=Solution().isSymmetric(root)
            

