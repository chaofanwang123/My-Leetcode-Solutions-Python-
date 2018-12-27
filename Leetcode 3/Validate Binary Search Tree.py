# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def BST(root):
            if root:
                if root.left==None and root.right==None:
                    return [True,root.val,root.val]
                if root.left==None:
                    Bool,minv,maxv=BST(root.right)
                    if Bool==False or minv<=root.val:
                        return [False,minv,maxv]      
                    return [True,root.val,maxv]
                if root.right==None:
                    Bool,minv,maxv=BST(root.left)
                    if Bool==False or maxv>=root.val:
                        return [False,minv,maxv]
                    return [True,minv,root.val] 
                Bool1,minv1,maxv1=BST(root.left)
                if Bool1==False or maxv1>=root.val:
                    return [False,minv1,maxv1]
                Bool2,minv2,maxv2=BST(root.right)
                if Bool2==False or minv2<=root.val:
                    return [False,minv2,maxv2]
                return [True,minv1,maxv2]
            return [True,0,0]
        if not root:
            return True
        Bool,minv,maxv=BST(root)
        return Bool

root=TreeNode(1)
root.left=TreeNode(1)

c=Solution().isValidBST(root)