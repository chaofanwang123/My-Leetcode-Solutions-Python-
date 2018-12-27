class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        rootl=self.trimBST(root.left,L,R)
        rootr=self.trimBST(root.right,L,R)
        if L<=root.val<=R:
            root.left=rootl
            root.right=rootr
            return root
        if rootl==None and rootr==None:
            return None
        if rootl==None:
            return rootr
        if rootr==None:
            return rootl
        p=rootl
        pre=p
        while p.right:
            pre=p
            p=p.right
        pre.right=None
        p.left=rootl
        p.right=rootr
        return p

root=TreeNode(1)
root.left=TreeNode(0)
root.right=TreeNode(2)
#root.left.left=TreeNode(5)
#root.right.right=TreeNode(7)

c=Solution().trimBST(root,1,2)