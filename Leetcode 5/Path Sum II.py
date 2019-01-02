# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def path(root,List,l,sum):
            if root:
                if root.left==None and root.right==None:
                    if root.val==sum:
                        List.append(l+[sum])
                    return
                if root.left:
                    path(root.left,List,l+[root.val],sum-root.val)
                if root.right:
                    path(root.right,List,l+[root.val],sum-root.val)
        if not root:
            return []
        List=[]
        path(root,List,[],sum)
        return List
                    
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
sum=30

c=Solution().pathSum(root,sum)              
            

