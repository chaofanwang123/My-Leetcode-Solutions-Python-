# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            if root and self.value==float('inf'):
                inorder(root.left)
                if self.count==k:
                    self.value=root.val
                self.count+=1
                inorder(root.right)
        self.value=float('inf')
        self.count=1
        inorder(root)
        return self.value

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.right=TreeNode(2)

c=Solution().kthSmallest(root,1)
