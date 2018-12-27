# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def rightorder(root):
            if root:
                rightorder(root.right)
                self.List.append(root.val+self.List[-1])
                rightorder(root.left)
        def inorder(root):
            if root:
                inorder(root.left)
                self.List.pop()
                root.val+=self.List[-1]
                inorder(root.right)
        if not root:
            return root
        self.List=[0]
        rightorder(root)
        inorder(root)
        return root

root=TreeNode(2)
root.left=TreeNode(1)

c=Solution().convertBST(root)

