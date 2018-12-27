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
        if not root:
            return None
        if p==root or q==root:
            return root
        if p.val>q.val:
            p,q=q,p
        node=root
        while node: 
            if p.val<node.val<q.val or node.val==p.val or node.val==q.val:
                return node
            if p.val<node.val:
                node=node.left
            else:
                node=node.right

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(30)
p=root.right
q=root.right.left

c=Solution().lowestCommonAncestor(root,p,q)