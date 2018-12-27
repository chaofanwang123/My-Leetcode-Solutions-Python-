# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumNumbers2(root,value):
            if root:
                value=value*10+root.val
                if root.left==None and root.right==None:
                    self.sum=self.sum+value
                if root.left:
                    sumNumbers2(root.left,value)
                if root.right:
                    sumNumbers2(root.right,value)
        if not root:
            return 0
        self.sum=0
        sumNumbers2(root,0)
        return self.sum

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)

c=Solution().sumNumbers(root)
