# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findpath(root,List,p):
            if root==p:
                List=List.insert(0,root)
                return True
            if not root:
                return False
            if findpath(root.left,List,p) or findpath(root.right,List,p):
                List=List.insert(0,root)
        List1=[]
        List2=[]
        findpath(root,List1,p)
        findpath(root,List2,q)
        i=0
        while i<len(List1) and i <len(List2) and List1[i]==List2[i]:
            i+=1
        return List1[i-1]

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
p=root
q=root.left.right
c=Solution().lowestCommonAncestor(root,p,q)

print(c.val)