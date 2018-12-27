# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        def dfs(root,depth,v,d):
            if root:
                if depth==d-1:
                    l=root.left
                    r=root.right
                    root.left=TreeNode(v)
                    root.right=TreeNode(v)
                    root.left.left=l
                    root.right.right=r
                elif depth<d-1:
                    if root.left:
                        root.left=dfs(root.left,depth+1,v,d)
                    if root.right:
                        root.right=dfs(root.right,depth+1,v,d)
                return root
        if d==1:
            p=TreeNode(v)
            p.left=root
            return p
        return dfs(root,1,v,d)

root=TreeNode(4)
root.left=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(1)

v=5
d=3
c=Solution().addOneRow(root,v,d)

