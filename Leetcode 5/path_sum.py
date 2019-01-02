class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

sum=18
root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(6)
root.left.left=TreeNode(2)
root.left.right=TreeNode(4)
root.right.right=TreeNode(7)

c=Solution().hasPathSum(root,sum)