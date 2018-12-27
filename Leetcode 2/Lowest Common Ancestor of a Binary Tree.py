# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findpath(root,List,p):
            if root==None:
                return False
            if root==p:
                List.insert(0,root)
                return True
            if findpath(root.left,List,p) or findpath(root.right,List,p):
                List.insert(0,root)
                return True
            return False
        List1=[]
        List2=[]
        findpath(root,List1,p)
        findpath(root,List2,q)
        i=0
        m=len(List1)
        n=len(List2)
        while i<m and i<n and List1[i]==List2[i]:
            i+=1
        return List1[i-1]

