# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None:
            return q==None
        if q:
            if p.val==q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False

p=TreeNode(1)
p.left=TreeNode(2)
p.right=TreeNode(3)

q=TreeNode(1)
q.left=TreeNode(2)
q.right=TreeNode(3)

c=Solution().isSameTree(None,q)
