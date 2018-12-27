# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder and preorder[0]:
            root=TreeNode(preorder[0])
            i=0
            while inorder[i]!=preorder[0]:
                i+=1
            root.left=self.buildTree(preorder[1:i+1],inorder[:i])
            root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
            return root
        else:
            return None

preorder = [1,2]
inorder = [2,1]
c=Solution().buildTree(preorder,inorder)
