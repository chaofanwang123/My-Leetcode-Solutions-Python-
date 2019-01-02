# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def preorder(root,list):
    if root:
        list.append(root.val)
        preorder(root.left,list)
        preorder(root.right,list)
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list=[]
        preorder(root,list)
        return list
root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(20)
root.left.left=TreeNode(3)
root.left.right=TreeNode(6)
root.right.left=TreeNode(15)

c=Solution().preorderTraversal(root)

